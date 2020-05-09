# conan-vcvrack-sdk
A conan recipe for the VCV Rack SDK for Rack plugin development.

[![Build Status](https://dev.azure.com/qnohot/qnohot/_apis/build/status/qno.conan-vcvrack-sdk?branchName=master)](https://dev.azure.com/qnohot/qnohot/_build/latest?definitionId=27&branchName=master)

[ ![Download](https://api.bintray.com/packages/qno/conan-public/vcvrack-sdk%3Avcvrack/images/download.svg?version=1.1.6%3Astable) ](https://bintray.com/qno/conan-public/vcvrack-sdk%3Avcvrack/1.1.6%3Astable/link)

# Usage

* Install and setup the [Conan C++ package manager](https://docs.conan.io/en/latest/installation.html) for your build platform
* ***Note:*** On the Windows platform there is no need to have the MinGW toolchain installed. It will be completely handled by Conan!
* On Windows create a [Conan profile](https://docs.conan.io/en/latest/reference/profiles.html) for MinGW under `<USER HOME>/.conan/profiles`, called e.g. `mingw`
    ```
    [settings]
    os=Windows
    os_build=Windows
    arch=x86_64
    arch_build=x86_64
    compiler=gcc
    compiler.version=8
    compiler.exception=seh
    compiler.libcxx=libstdc++11
    compiler.threads=posix
    build_type=Release
    [options]
    [build_requires]
    mingw_installer/1.0@conan/stable
    msys2/20190524
    [env]
    ```
* Add the following conan remotes:
  * `conan remote add qno https://api.bintray.com/conan/qno/conan-public`

* For developing a Rack plugin with conan-vcvrack-sdk see [conan-vcvrack-sdk-plugin-example](https://github.com/qno/conan-vcvrack-sdk-plugin-example) for an example
