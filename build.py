import os
import shutil

def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Command failed: %s" % cmd)

def init_folders():
    shutil.rmtree("ctoot/build", ignore_errors=True)
    shutil.rmtree("moduru/build", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    os.mkdir("build")

# Visual Studio
init_folders()

if os.path.exists("moduru"):
	run("cd moduru && git pull && cd")
else:
	run("git clone https://github.com/izzyreal/moduru")
	
if os.path.exists("ctoot"):
	run("cd ctoot && git pull && cd")
else:
	run("git clone https://github.com/izzyreal/ctoot")

os.chdir("build")
run("conan workspace install ../conanws_vs.yml")
run("conan workspace install ../conanws_vs.yml -s build_type=Debug")
run('cmake .. -G "Visual Studio 15 Win64"')
#run('cmake --build . --config Release')
#run('cmake --build . --config Debug')
#os.chdir("..")
#run('cd moduru/build/Release && test')
#run('cd moduru/build/Debug && test')
