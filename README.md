# Intended Audience

You are interested in

* contributing to VMPC2000XL
* building vMPC2000XL for specific platforms/environments
* exploring music and audio source code
* C++ IDE workspace creation (Xcode/Visual Studio) with [Conan](https://conan.io/)
* C++ build automation and package management with [Conan](https://conan.io/)

# Quick start

Requirements:
- Visual Studio 2019, Xcode or Make
- [CMake](https://cmake.org/)
- [Python](https://www.python.org/downloads/)
- [Conan](https://docs.conan.io/en/latest/installation.html)

Once you have these tools installed, run the following commands:
```
conan remote add jfrog-izmar https://izmar.jfrog.io/artifactory/api/conan/dev
git clone https://github.com/izzyreal/vmpc-workspace
cd vmpc-workspace
```
If you want to use Visual Studio and build 64 bit binaries, run
```
python build.py vs
```
or for a 32 bit
```
python build.py vs32
```
and for Xcode
```
python build.py xcode
```

There are some more generators available. Run `python build.py` to see them all. The ninja and make generators are used by after executing `build.py` going into the `vmpc-workspace/build` dir and running `make help` or `ninja help` to see the available targets.

For Xcode and VS, open the solution or project in `vmpc-workspace/build` and you're good to go. There are Release and Debug configs. Both IDEs will default to the Debug config.


# Overview

The aim of `vmpc-workspace` is to give you everything that you need to create an IDE project/solution/workspace for navigating, building and contributing to the VMPC2000XL source code.

If you are only interested in building vMPC2000XL, you are better off with the [`vmpc-juce`](https://github.com/izzyreal/vmpc-juce) project.

If you simply want to use vMPC2000XL and need the installer, see [http://www.izmar.nl/index.php/downloads](http://www.izmar.nl/index.php/downloads).



# Packages

#### vmpc-juce

`vmpc-juce` is a runnable GUI implementation of `mpc`, based on JUCE6. The root of the workspace, and thus of the dependency tree, `vmpc-juce` is where the main application's executable lives. `vmpc` depends on `mpc`, `ctoot` and `moduru` (and some 3rd party transitive dependencies that are beyond the scope of this readme).


#### mpc

`mpc` compiles to a static library that covers most of the [Akai MPC](https://en.wikipedia.org/wiki/Akai_MPC) problem domain. The MPC's core functionalities are:

- sequencing, musical arrangement
- sample record and playback

The library is agnostic to GUI implementation, and depends on `ctoot` and `moduru`.



#### ctoot

`ctoot` is an attempt to bring Steve Taylor's [`toot2`](https://github.com/toot/toot2) from Java to C++. In many areas only the bare minimum is implemented, so don't expect a full port. Most of the fundamentals of the digital audio and music problem domain is covered however:

- audio system with mixer (optionally auto-connecting)
- modular configuration of inputs, outputs and other DSP processes
- audio process service discovery (for e.g. effects and synthesizers)
- delay, reverb, EQ, dynamics
- synthesis
- MIDI system (optionally auto-connecting)

  
#### moduru

`moduru` is a collection of utilities I made, combined some easy to include 3rd party libraries that I like to use, for example `libsamplerate`.


# Development Setup (Visual Studio 2017 & Xcode)

Follow the Quick Start instructions above.

There are 4 main targets, and 1 test suite target for each of them. Note that the test suite targets are completely different from Conan's `test_package` directories. The latter are concerned with verifying the health of a Conan package, and verifying inclusion of headers and linked libraries. The test suites of the main targets are for unit and integration testing.

So the target list of the workspace becomes:

- `vmpc2000xl_Standalone` (executable)
- `mpc` (static library)
- `mpc-tests` (executable)
- `ctoot` (static library)
- `ctoot-tests` (executable)
- `moduru` (static library)
- `moduru-tests` (executable)

The `vmpc-workspace` directories [`vmpc-juce`](https://github.com/izzyreal/vmpc-juce), [`mpc`](https://github.com/izzyreal/mpc), [`ctoot`](https://github.com/izzyreal/ctoot) and [`moduru`](https://github.com/izzyreal/moduru) are created by successful execution of the python build script. These directories are pulled from the linked repositories.
