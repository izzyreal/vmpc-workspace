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
parser.add_argument('ide', help='The IDE you want to build the workspace for. Options are vs and xcode')

args = parser.parse_args()

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Command failed: %s" % cmd)

def init_folders():
    shutil.rmtree("vmpc/build", ignore_errors=True)
    shutil.rmtree("mpc/build", ignore_errors=True)
    shutil.rmtree("ctoot/build", ignore_errors=True)
    shutil.rmtree("moduru/build", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    if not os.path.exists("build"):
         os.mkdir("build")

if args.ide != 'vs' and args.ide != 'xcode':
    print('ide has to be vs or xcode')
    quit()

init_folders()

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

if os.path.exists("vmpc"):
	run("cd vmpc && git pull && cd")
else:
	run("git clone https://github.com/izzyreal/vmpc")

os.chdir("build")
run("conan workspace install ../conanws.yml --build missing")
run("conan workspace install ../conanws.yml -s build_type=Debug --build missing")

if args.ide == 'vs':
    run('cmake .. -G "Visual Studio 15 Win64"')
elif args.ide == 'xcode':
	run('cmake .. -G "Xcode"')

# Uncomment the below to build an executable
#run('cmake --build . --config Release')
#run('cmake --build . --config Debug')

# Uncommend the below to run the executables
#os.chdir("..")
#run('cd moduru/build/Release && test')
#run('cd moduru/build/Debug && test')
