#!/bin/sh

cd ~/git/vmpc-workspace
python3 build.py -c xcode
cd build
cmake --build . --config Release --target vmpc2000xl_All
