import os, stat
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from conans.errors import ConanInvalidConfiguration


class VCVRackSDKConan(ConanFile):
    name = "vcvrack-sdk"
    version = "1.1.6"
    license = "GPL-3.0"
    author = "Andrew Belt"
    url = "https://github.com/qno/conan-vcvrack-sdk"
    homepage = "https://vcvrack.com"
    description = "VCV Rack SDK for Rack plugin development."

    settings = "os", "compiler", "arch"

    _SDK_DIR = "Rack-SDK"

    def configure(self):
        if self._isVisualStudioBuild:
            self.output.error("Rack SDK on Windows is only compatible with MinGW GCC toolchain!")
            raise ConanInvalidConfiguration("VCV Rack SDK is not compatible with Visual Studio!")

        if self.settings.arch != "x86_64":
            raise ConanInvalidConfiguration("VCV Rack SDK currently only supports x86_64 platform!")

    def requirements(self):
        if self.settings.os == "Windows":
            self.requires.add("msys2/20190524")

    def system_requirements(self):
        packages = ["git", "curl", "wget", "unzip", "zip", "cmake", "jq"]
        update_installer = True

        if self.settings.os == "Windows":
            self.output.warn("manipulate script internal environment - add MSYS_BIN to PATH for using pacman tool")
            del os.environ["CONAN_SYSREQUIRES_SUDO"]
            os.environ["PATH"] += os.pathsep + self.env["MSYS_BIN"]
            packages = ["git", "wget", "make", "tar", "unzip", "zip",
                        "mingw-w64-x86_64-jq", "mingw-w64-x86_64-libwinpthread", "mingw-w64-x86_64-cmake"]
            update_installer = False

        if self.settings.os == "Macos":
            packages += ["autoconf", "automake", "libtool"]

        installer = SystemPackageTool()
        for package in packages:
            installer.install(package, update=update_installer)

    def build(self):
        url = "https://vcvrack.com/downloads/Rack-SDK-{}.zip".format(self.version)
        self.output.info("Downloading {}".format(url))
        tools.get(url)

    def package(self):
        self.copy("*.*", dst="include", src="{}/include".format(self._SDK_DIR))
        self.copy("*.*", dst="dep", src="{}/dep".format(self._SDK_DIR))
        self.copy("*.mk", dst=".", src="{}".format(self._SDK_DIR))
        os.chmod(os.path.join(self._SDK_DIR, "helper.py"), stat.S_IRWXU|stat.S_IRGRP|stat.S_IROTH)
        self.copy("helper.py", dst="script", src="{}".format(self._SDK_DIR))

        if self.settings.os == "Windows":
            self.copy("*Rack*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.settings.os == "Windows":
            self.cpp_info.cppflags.append("-DARCH_WIN")
            self.cpp_info.libs.append("Rack")
            self.env_info.path.append(os.path.join(self.deps_env_info["msys2"].MSYS_ROOT, "mingw64", "bin"))

        if self.settings.os == "Linux":
            self.cpp_info.cppflags.append("-DARCH_LIN")

        if self.settings.os == "Macos":
            self.cpp_info.cppflags.append("-DARCH_MAC")

        self.cpp_info.includedirs = ["include", "dep/include"]
        self.env_info.path.append(os.path.join(self.package_folder, "script"))

    def package_id(self):
       self.info.header_only()

    @property
    def _isMinGWBuild(self):
        return self.settings.os == "Windows" and self.settings.compiler == "gcc"

    @property
    def _isVisualStudioBuild(self):
        return self.settings.os == "Windows" and self.settings.compiler == "Visual Studio"
