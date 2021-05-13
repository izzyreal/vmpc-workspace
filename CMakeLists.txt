cmake_minimum_required(VERSION 3.0)
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_OSX_SYSROOT /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
project(vmpc-workspace)

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)
conan_workspace_subdirectories()
