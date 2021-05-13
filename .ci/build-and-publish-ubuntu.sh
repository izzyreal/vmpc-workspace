#!/bin/sh

cd ~/git/vmpc-workspace
python3 build.py -c ninja
cd build
ninja -f build-Release.ninja vmpc2000xl_All
