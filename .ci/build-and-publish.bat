cd \Users\izmar\git\vmpc-workspace
python build.py -c vs
cd build
cmake --build . --config Release --target vmpc2000xl_All

cd ..
cd ..
cd vmpc-workspace-32
python build.py -c vs32
cd build
cmake --build . --config Release --target vmpc2000xl_All

cd \Users\izmar\git\vmpc-binaries
git pull

iscc \Users\izmar\git\vmpc-installer-scripts\win\vmpc.iss

git add installers

FOR /F "tokens=*" %a in ('get-version.cmd') do SET VERSION=%a

git commit -m "Publish %VERSION% Windows"
git push
