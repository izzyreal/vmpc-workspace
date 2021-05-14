#!/bin/sh

cd ~/git/vmpc-workspace
python3 build.py -c xcode
cd build
cmake --build . --config Release --target vmpc2000xl_All

packagesbuild ~/git/vmpc-installer-scripts/mac/VMPC2000XL.pkgproj

cd ~/git/vmpc-binaries
git add installers

VERSION=$(defaults read ~/git/vmpc-workspace/vmpc-juce/build/vmpc2000xl_artefacts/Release/Standalone/VMPC2000XL.app/Contents/Info CFBundleShortVersionString)

git commit -m "Publish $VERSION MacOS"
git push
