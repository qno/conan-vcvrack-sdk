# conan-vcvrack-sdk
A conan recipe for the VCV Rack SDK for Rack plugin development.

[![Build Status](https://dev.azure.com/qnohot/qnohot/_apis/build/status/qno.conan-vcvrack-sdk?branchName=master)](https://dev.azure.com/qnohot/qnohot/_build/latest?definitionId=27&branchName=master)

[Show artifact at JFrog](https://qno.jfrog.io/ui/repos/tree/General/public-conan-local%2Fvcvrack%2Fvcvrack-sdk)

# Usage

* Install and setup the [Conan C++ package manager](https://docs.conan.io/en/latest/installation.html) for your build platform

* Add the following conan remote:
  * `conan remote add qno https://qno.jfrog.io/artifactory/api/conan/public-conan`

* Recipe reference `vcvrack-sdk/1.1.6@vcvrack/stable`

* For developing a Rack plugin with conan-vcvrack-sdk see [conan-vcvrack-sdk-plugin-example](https://github.com/qno/conan-vcvrack-sdk-plugin-example) for an example
