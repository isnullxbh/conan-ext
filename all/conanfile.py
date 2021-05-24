import os

from conans import ConanFile, tools


class ExtConan(ConanFile):
    name = "ext"
    license = "MIT"
    author = "Oleg E. Vorobiov isnullxbh@gmail.com"
    url = "https://github.com/isnullxbh/conan-ext"
    description = "The C++ standard library extensions"
    topics = ("cpp", "cpp20", "cpp-library")
    # settings = "os", "compiler", "build_type", "arch"
    # options = {"shared": [True, False], "fPIC": [True, False]}
    # default_options = {"shared": False, "fPIC": True}
    # generators = "cmake"

    _source_subfolder = "source_subfolder"

    def package_id(self):
        self.info.header_only()

    def source(self):
        tools.get(**self.conan_data["sources"][self.version], strip_root=True, destination=self._source_subfolder)

    def package(self):
        include_dir = os.path.join(self._source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy(pattern="*.hpp", dst="include", src=include_dir)
