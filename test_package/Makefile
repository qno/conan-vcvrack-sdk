CONAN_BUILD_INFO_FILE=$(wildcard **/**/conanbuildinfo.mak)

include $(CONAN_BUILD_INFO_FILE)

RACK_DIR ?= $(CONAN_ROOT_VCVRACK-SDK-INSTALLER)
RACK_USER_DIR ?= testuserdir

SOURCES += $(wildcard *.cpp)

# Include the Rack plugin Makefile framework
include $(RACK_DIR)/plugin.mk
