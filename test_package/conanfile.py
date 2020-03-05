import os

from conans import ConanFile, CMake, AutoToolsBuildEnvironment, tools
from conans.tools import os_info, SystemPackageTool


class VCVRackSDKTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "make"

    def imports(self):
        self.copy("helper.py", src="script")

    def build(self):
        self._buildWithCMake()
        self._buildWithMake()

    def test(self):
        self.output.info("check for helper.py availability")
        self.run("python helper.py")

    def _buildWithCMake(self):
        self.output.info("building test plugin with CMake ...")
        cmake = CMake(self)
        cmake.configure(build_dir="cmake-build")
        cmake.build(build_dir="cmake-build")

    def _buildWithMake(self):
        self.output.info("building test plugin with Make ...")
        with tools.chdir("../.."):
            autotools = AutoToolsBuildEnvironment(self)
            autotools.make()
