import os

from conans import ConanFile, CMake, AutoToolsBuildEnvironment, tools
from conans.tools import os_info, SystemPackageTool


class VCVRackSDKInstallerTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "make"

    exports_sources = "*"

    def system_requirements(self):
        if self.settings.os == "Windows":
            os.environ["PATH"] += os.pathsep + os.pathsep.join(self.env["PATH"]) + os.pathsep + "c:\\.conan\\80265f\\1\\bin\\mingw64\\bin"

    def build(self):
        self.output.info("generate plugin src just with helper?")
        self._buildWithCMake()
        self._buildWithMake()

    def test(self):
        self.output.info("nothing to run here")

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
