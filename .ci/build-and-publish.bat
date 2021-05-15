cd \Users\izmar\git\vmpc-workspace
rem python build.py -c vs
cd build
rem cmake --build . --config Release --target vmpc2000xl_All

cd ..
cd ..
cd vmpc-workspace-32
rem python build.py -c vs32
cd build
rem cmake --build . --config Release --target vmpc2000xl_All

cd \Users\izmar\git\vmpc-binaries
git pull

iscc \Users\izmar\git\vmpc-installer-scripts\win\vmpc.iss

git add installers

FOR /F "tokens=*" %%a in ('\Users\izmar\git\vmpc-workspace\.ci\get-version.cmd') do SET VERSION=%%a

git commit -m "Publish %VERSION% Windows"
git push https://user:pw@github.com/izzyreal/vmpc-binaries