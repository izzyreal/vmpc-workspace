# Intended Audience

You are interested in

* exploring music and audio source code
* contributing to VMPC2000XL
* C++ IDE workspace creation (Xcode/Visual Studio) with [Conan](https://conan.io/)

- C++ build automation and package management with [Conan](https://conan.io/)

  

# Overview

The aim of `vmpc-workspace` is to give you everything that you need to create an IDE project/solution/workspace for exploring, building and contributing to the VMPC2000XL source code.

If you are only interested in building VMPC2000XL, you are better off with the [`vmpc`](https://github.com/izzyreal/vmpc) project.

If you simply want to use VMPC2000XL and need the installer, see [http://www.izmar.nl/index.php/downloads](http://www.izmar.nl/index.php/downloads).



# Packages

Early 2019 I developed a strong interest in C++ package management. VMPC2000XL had been using [JUCE](https://juce.com/) for a while, but I disliked how it demands to sit at the top of one's dependency chain. JUCE comes with the [Projucer](https://juce.com/discover/stories/projucer-manual), an application that is required in order to produce workspaces for your IDE. I find that cumbersome -- I see more merit in generic approaches, e.g. [Cmake](https://cmake.org/). I want to use the tooling I prefer when consuming a dependency. Additionally, the Projucer wouldn't let me create additional targets within the same workspace, so editing code of both the JUCE project as well as of my own libraries wasn't effortless.

JUCE does many amazing things, but I really wanted to learn more about generic C++ and build tooling, and C++ package management.

I ended up using Conan, which plays nice with Cmake, to orchestrate workspaces, builds and packages. I started by wrapping the smallest of my libraries, `moduru`, into a Conan package. Then `ctoot`, `mpc`, `vmpc` and finally this repository's project — `vmpc-workspace`.



#### vmpc

`vmpc` is a runnable GUI implementation of `mpc`. The root of the workspace, and thus of the dependency tree, it's where the main application's executable lives. `vmpc` depends on `mpc`, `ctoot` and `moduru` (and many 3rd party libraries).



#### mpc

`mpc` compiles to a static library that covers most of the [Akai MPC](https://en.wikipedia.org/wiki/Akai_MPC) problem domain. The MPC's core functionalities are:

- sequencing, musical arrangement
- sample record and playback

The library is agnostic to GUI implementation, and depends on `ctoot` and `moduru`.



#### ctoot

`ctoot` is an attempt to bring Steve Taylor's [`toot2`](https://github.com/toot/toot2) from Java to C++. In many areas only the bare minimum is implemented, so don't expect a full translation. Much of the basics of the digital audio and music problem domain is covered however:

- audio servers to interface with audio devices

- audio system with mixer (optionally auto-connecting)

- modular configuration of inputs, outputs and other DSP processes

- audio process service discovery (for e.g. effects and synthesizers)

- delay, reverb, EQ, dynamics

- synthesis

- MIDI system (optionally auto-connecting)

  

#### moduru

`moduru` is a messy collection of utilities I made, combined some easy to include 3rd party libraries that I like to use like `libsamplerate`. It needs a lot of work, if not be removed from the project after coming up with alternatives.



# Development Setup (Visual Studio & Xcode)

Requirements:

- [Python](https://www.python.org/downloads/)
- [Conan](https://docs.conan.io/en/latest/installation.html)

After cloning this repo, enter it and run `python build.py vs` or `python build.py xcode`. You will now have a Visual Studio solution or Xcode project in the `build` directory. Inside VS or Xcode you can choose to build debug or release.

There are 4 main targets, and 1 test suite target for each of them. Note that the test suite targets are completely different from Conan's `test_package` directories. The latter are concerned with verifying the health of a Conan package, and verifying inclusion of headers and linked libraries. The test suites of the main targets are for unit and integration testing.

So the target list of the workspace becomes:

- `vmpc` (executable) 
- `vmpc-tests` (executable)
- `mpc` (static library)
- `mpc-tests` (executable)
- `ctoot` (static library)
- `ctoot-tests` (executable)
- `moduru` (static library)
- `moduru-tests` (executable)

The `vmpc-workspace` directories [`vmpc`](https://github.com/izzyreal/vmpc), [`mpc`](https://github.com/izzyreal/mpc), [`ctoot`](https://github.com/izzyreal/ctoot) and [`moduru`](https://github.com/izzyreal/moduru) are created by a successful execution of the python build script. These directories are pulled from the linked repositories.