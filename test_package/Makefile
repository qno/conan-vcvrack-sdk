include conanbuildinfo.mak

SLUG := FAKE
VERSION := FAKE

RACK_DIR ?= $(CONAN_ROOT_VCVRACK-SDK-INSTALLER)
RACK_USER_DIR ?= testuserdir

CFLAGS          += $(CONAN_CFLAGS)
CXXFLAGS        += $(CONAN_CXXFLAGS)
CPPFLAGS        += $(addprefix -I, $(CONAN_INCLUDE_DIRS))
CPPFLAGS        += $(addprefix -D, $(CONAN_DEFINES))
LDFLAGS         += $(addprefix -L, $(CONAN_LIB_DIRS))
LDLIBS          += $(addprefix -l, $(CONAN_LIBS))

SOURCES += $(wildcard *.cpp)

# Include the Rack plugin Makefile framework
include $(RACK_DIR)/plugin.mk
