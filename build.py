import os
import shutil
import argparse
import sys

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

parser = MyParser(description='Build the vmpc2000xl workspace.')
parser.add_argument('buildtool', help='The build tool you want to build the workspace for. Options are vs, xcode and ninja.')
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

if args.buildtool != 'vs' and args.buildtool != 'xcode' and args.buildtool != 'ninja':
    print('Build tool has to be vs, xcode or ninja')
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
		run("git clone https://github.com/izzyreal/vmpc-juce")

os.chdir("build")
run("conan workspace install ../conanws.yml --build missing")
run("conan workspace install ../conanws.yml -s build_type=Debug --build missing")

if args.buildtool == 'vs':
    run('cmake .. -G "Visual Studio 16 2019"')
elif args.buildtool == 'xcode':
    run('cmake .. -G "Xcode"')
elif args.buildtool == 'ninja':
    run('cmake .. -G "Ninja Multi-Config"')

# Uncomment the below to build an executable
run('cmake --build . --config Release --target vmpc2000xl_Standalone')
#run('cmake --build . --config Debug')

# Uncommend the below to run the executables
#os.chdir("..")
#run('cd moduru/build/Release && test')
#run('cd moduru/build/Debug && test')
