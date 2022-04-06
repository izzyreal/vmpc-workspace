# VMPC2000XL IDE workspace build script intended for contributors
# and others who are interested in poking around in VMPC2000XL's code.
#
# This script creates multi-config project files for your
# IDE. Supported IDEs are Code::Blocks, Visual Studio and Xcode.
#
# Once you load the created project file from the root build/ dir
# into your IDE, you can switch between Debug and Release configurations.


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
parser.add_argument('buildtool', help='The build tool you want to build the workspace for.\nOptions are vs, vs32, vs2022, xcode, xcode-ios, make, codeblocks, ninja, ninja-multi (same as ninja) and ninja-single.')
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
    shutil.rmtree("akaifat/build", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)

if args.buildtool not in ['vs', 'vs32', 'vs2022', 'xcode','xcode-ios', 'ninja-single', 'ninja-multi', 'ninja', 'codeblocks', 'make']:
    print('Build tool has to be vs, vs32, vs2022, xcode, xcode-ios, make, codeblocks, ninja, ninja-multi or ninja-single')
    quit()

if args.clean == True:
    clean_folders()

if not os.path.exists("build"):
    os.mkdir("build")

if args.offline == False:
    if os.path.exists("akaifat"):
        run("cd akaifat && git pull && cd")
    else:
        run("git clone https://github.com/izzyreal/akaifat")
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
if args.buildtool == 'vs2022':
    run('cmake .. -G "Visual Studio 17 2022"')
elif args.buildtool == 'vs32':
    run('cmake .. -G "Visual Studio 16 2019" -A Win32')
elif args.buildtool == 'xcode':
    run('cmake .. -G "Xcode"')
elif args.buildtool == 'xcode-ios':
    run('cmake .. -G "Xcode" -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=9.3 -DCMAKE_TOOLCHAIN_FILE=../ios.toolchain.cmake -DPLATFORM=OS64COMBINED -DENABLE_ARC=0')
elif args.buildtool == 'ninja' or args.buildtool == 'ninja-multi':
    run('cmake .. -G "Ninja Multi-Config"')
elif args.buildtool == 'codeblocks':
    run('cmake .. -G "CodeBlocks - Ninja"')
elif args.buildtool == 'ninja-single':
    run('cmake .. -G "Ninja" -DCMAKE_BUILD_TYPE=Debug -B ./Debug')
    run('cmake .. -G "Ninja" -DCMAKE_BUILD_TYPE=Release -B ./Release')
elif args.buildtool == 'make':
    run('cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Debug -B ./Debug')
    run('cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release -B ./Release')
