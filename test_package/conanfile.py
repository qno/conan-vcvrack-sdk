import os

from conans import ConanFile, CMake, AutoToolsBuildEnvironment, tools


class VCVRackSDKInstallerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "make"

    exports_sources = "*"

    def build(self):
        self.output.info("generate stuff with helper first?")
        self._buildWithCMake()
        self._buildWithMake()

    def test(self):
        self.output.info("Rack SDK test ...?")

    def _buildWithCMake(self):
        cmake = CMake(self)
        cmake.configure(build_dir="cmake-build")
        cmake.build(build_dir="cmake-build")

    def _buildWithMake(self):
        self.output.info("Todo ... build Rack SDK test with make...?")
        autotools = AutoToolsBuildEnvironment(self)
        autotools.make(target="-f ../../Makefile")
