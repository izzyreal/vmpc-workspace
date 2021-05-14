#!/bin/sh

cd ~/git/vmpc-workspace
python3 build.py -c xcode
cd build
cmake --build . --config Release --target vmpc2000xl_All

packagesbuild ~/git/vmpc-installer-scripts/mac/VMPC2000XL.pkgproj

cd ~/git/vmpc-binaries
git add installers
git commit -m "Publish $VERSION MacOS"
git push
