# conan-ext

A Conan recipe for the ext library

## Getting started

### Prerequisites

- Python 3
- Conan package manager
- Compiler with C++20 support

### Creating package

```shell
# Copy the recipe to the local cache
conan export . ext/0.1.4@_/_

# Install the requirements specified in the recipe
conan install ext/0.1.4@_/_ --build=ext --profile=gcc -s compiler.cppstd=20 -o ext:header_only=False

# Test a package
conan test test_package ext/0.1.4@_/_ --profile=gcc -s compiler.cppstd=20
```

### Uploading package

```shell
conan upload ext/0.1.4@_/_ --all -r isnullxbh/testing
```

## Contact

Oleg E. Vorobiov <isnullxbh@gmail.com>
