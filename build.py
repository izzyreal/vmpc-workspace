import os
import shutil
import argparse
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(description='Build the VMPC2000XL workspace.')
parser.add_argument('buildtool', help='The build tool you want to build the workspace for.\nOptions are vs, vs32, xcode, make, ninja, ninja-multi (same as ninja) and ninja-single.')
parser.add_argument('-o', '--offline', action='store_true', help='Offline mode. No git clone or pull and no Conan package fetching.')
parser.add_argument('-c', '--clean', action='store_true', help='Clean all build dirs before building.')

args = parser.parse_args()

if args.offline == True:
	sys.stderr.write('Entering offline mode...\n')

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Command failed: %s" % cmd)

def clean_folders():
    shutil.rmtree("vmpc-juce/build", ignore_errors=True)
    shutil.rmtree("mpc/build", ignore_errors=True)
    shutil.rmtree("ctoot/build", ignore_errors=True)
    shutil.rmtree("moduru/build", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)

if args.buildtool != 'vs' and args.buildtool != 'vs32' and args.buildtool != 'xcode' and args.buildtool != 'ninja-single'and args.buildtool != 'ninja-multi'and args.buildtool != 'ninja' and args.buildtool != 'make':
    print('Build tool has to be vs, vs32, xcode, make, ninja, ninja-multi or ninja-single')
    quit()

if args.clean == True:
    clean_folders()

if not os.path.exists("build"):
    os.mkdir("build")

if args.offline == False:
	if os.path.exists("moduru"):
		run("cd moduru && git pull && cd")
	else:
		run("git clone https://github.com/izzyreal/moduru")

	if os.path.exists("ctoot"):
		run("cd ctoot && git pull && cd")
	else:
		run("git clone https://github.com/izzyreal/ctoot")

	if os.path.exists("mpc"):
		run("cd mpc && git pull && cd")
	else:
		run("git clone https://github.com/izzyreal/mpc")

	if os.path.exists("vmpc-juce"):
		run("cd vmpc-juce && git pull && cd")
	else:
		run("git clone --single-branch --branch lv2 https://github.com/izzyreal/vmpc-juce")

os.chdir("build")
if args.buildtool == 'vs32':
	run("conan workspace install ../conanws.yml -s arch_build=x86 --build missing")
	run("conan workspace install ../conanws.yml -s arch_build=x86 -s build_type=Debug --build missing")
elif args.buildtool == 'make' or args.buildtool == 'ninja-single':
    if not os.path.exists("Debug"): os.mkdir("Debug")
    if not os.path.exists("Release"): os.mkdir("Release")
    run("cd Release && conan workspace install ../../conanws.yml --build missing && cd ..")
    run("cd Debug && conan workspace install ../../conanws.yml --build missing -s build_type=Debug && cd ..")
else:
	run("conan workspace install ../conanws.yml --build missing")
	run("conan workspace install ../conanws.yml --build missing -s build_type=Debug")

if args.buildtool == 'vs':
    run('cmake .. -G "Visual Studio 16 2019"')
elif args.buildtool == 'vs32':
    run('cmake .. -G "Visual Studio 16 2019" -A Win32')
elif args.buildtool == 'xcode':
    run('cmake .. -G "Xcode"')
elif args.buildtool == 'ninja' or args.buildtool == 'ninja-multi':
    run('cmake .. -G "Ninja Multi-Config"')
elif args.buildtool == 'ninja-single':
    run('cmake .. -G "Ninja" -DCMAKE_BUILD_TYPE=Debug -B ./Debug')
    run('cmake .. -G "Ninja" -DCMAKE_BUILD_TYPE=Release -B ./Release')
elif args.buildtool == 'make':
    run('cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug -B ./Debug')
    run('cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -B ./Release')

# Uncomment the below to build a target
# When using Unix Makefiles or Ninja single config
#run('cmake --build ./Release --config Release --target vmpc2000xl_LV2')

# When using any other generator
#run('cmake --build . --config Release --target vmpc2000xl_Standalone')

# Uncommend the below to run the executables
#os.chdir("..")
#run('cd moduru/build/Release && test')
#run('cd moduru/build/Debug && test')
