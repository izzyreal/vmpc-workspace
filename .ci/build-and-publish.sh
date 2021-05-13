#!/bin/sh

cd ~/git/vmpc-workspace
python build.py -c xcode
cd build
cmake --build . --config Release --target vmpc2000xl_All
