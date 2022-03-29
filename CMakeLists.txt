cmake_minimum_required(VERSION 3.0)
set(CMAKE_CXX_STANDARD 17)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)
project(vmpc-workspace)

if(APPLE)
  if (IOS)
    execute_process(
      COMMAND python macos-codesign-details-extractor.py
      WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
      OUTPUT_VARIABLE DEVELOPMENT_TEAM)
    set(CMAKE_XCODE_ATTRIBUTE_DEVELOPMENT_TEAM "${DEVELOPMENT_TEAM}")
    message("\nSetting macOS/iOS development team to organisational unit: ${DEVELOPMENT_TEAM}\n"
      "This is derived from the first valid Apple Development certificate in your local keychain.\n"
      "You can tweak it in the Build Settings tab of your root project.\n")
  else()
    set(CMAKE_OSX_SYSROOT /Library/Developer/CommandLineTools/SDKs/MacOSX.sdk)
endif()
endif()

include(${CMAKE_BINARY_DIR}/conanworkspace.cmake)
conan_workspace_subdirectories()
