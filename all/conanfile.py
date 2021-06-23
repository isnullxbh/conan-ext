import os

from conans import ConanFile, CMake, tools


class ExtConan(ConanFile):
    name = "ext"
    license = "MIT"
    author = "Oleg E. Vorobiov isnullxbh@gmail.com"
    url = "https://github.com/isnullxbh/conan-ext"
    description = "The C++ standard library extensions"
    topics = ("cpp", "cpp20", "cpp-library")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], "header_only": [True, False]}
    default_options = {"shared": False, "fPIC": True, "header_only": True}
    generators = "cmake"

    _source_subfolder = "source_subfolder"

    def configure(self):
        if self.options.header_only:
            self.settings.clear()
            del self.options.shared
            del self.options.fPIC

    def package_id(self):
        if self.options.header_only:
            self.info.header_only()

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True, destination=self._source_subfolder)

    def build(self):
        if not self.options.header_only:
            cmake = CMake(self)
            cmake.configure(source_folder=self._source_subfolder)
            cmake.build()

    def package(self):
        inc_dir = os.path.join(self._source_subfolder, "include")
        src_dir = os.path.join(self._source_subfolder, "src")

        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=inc_dir)
        self.copy(pattern="*.cpp", dst="src", src=src_dir)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.so", dst="lib", keep_path=False)
        self.copy(pattern="*.dylib", dst="lib", keep_path=False)
        self.copy(pattern="*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.options.header_only:
            self.cpp_info.defines.append("HEADER_ONLY")
        else:
            self.cpp_info.libs = ["ext"]
