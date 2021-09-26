#!/bin/sh

cd ~/git/vmpc-workspace
git pull
python3 build.py -c ninja
cd build
ninja -f build-Release.ninja vmpc2000xl_All

cd ~/git/vmpc-binaries

git pull

./copy_bin_ubuntu18_x86_64.sh

git add linux

git commit -m "Publish 0.4 Ubuntu x86_64"
git push