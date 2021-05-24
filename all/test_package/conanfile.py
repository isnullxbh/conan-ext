import os

from conans import ConanFile, CMake, tools


class ExtTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_dir = os.path.join("bin", "test_package")
        self.run(bin_dir, run_environment=True)
