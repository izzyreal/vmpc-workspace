cmake_minimum_required(VERSION 3.0)
set(CMAKE_CXX_STANDARD 17)

project(vmpc-workspace)

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)
conan_workspace_subdirectories()