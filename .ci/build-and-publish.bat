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
