from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os

class VCVRackSDKInstallerConan(ConanFile):
    name = "vcvrack-sdk-installer"
    version = "1.1.6"
    license = "GPL-3.0"
    author = "Andrew Belt"
    url = "https://github.com/qno/conan-vcvrack-sdk-installer"
    homepage = "https://vcvrack.com"
    description = "VCV Rack SDK for Rack plugin development."

    settings = "os", "compiler", "build_type", "arch"

    _SDK_DIR = "Rack-SDK"

    def configure(self):
        if self._isVisualStudioBuild:
            self.output.error("Rack SDK on Windows is only compatible with MinGW GCC toolchain!")
            raise ConanInvalidConfiguration("VCV Rack SDK is not compatible with Visual Studio!")

    def build(self):
        url = "https://vcvrack.com/downloads/Rack-SDK-{}.zip".format(self.version)
        self.output.info("Downloading {}".format(url))
        tools.get(url)

    def package(self):
        self.copy("*.*", dst="include", src="{}/include".format(self._SDK_DIR))
        self.copy("*.*", dst="dep", src="{}/dep".format(self._SDK_DIR))

        if self.settings.os == "Windows":
            self.copy("*Rack*.a", dst="lib", keep_path=False)

    def package_info(self):

        if self.settings.os == "Windows":
            self.cpp_info.cppflags.append("-DARCH_WIN")
            self.cpp_info.libs.append("Rack")

        if self.settings.os == "Linux":
            self.cpp_info.cppflags.append("-DARCH_LIN")

        if self.settings.os == "Macos":
            self.cpp_info.cppflags.append("-DARCH_MAC")

        self.cpp_info.includedirs = ["include", "dep/include"]

    def package_id(self):
       del self.info.settings.compiler
       del self.info.settings.os
       del self.info.settings.build_type

    @property
    def _isMinGWBuild(self):
        return self.settings.os == "Windows" and self.settings.compiler == "gcc"

    @property
    def _isVisualStudioBuild(self):
        return self.settings.os == "Windows" and self.settings.compiler == "Visual Studio"
