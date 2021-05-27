# conan-ext

A Conan recipe for the ext library

## Getting started

### Prerequisites

- Python 3
- Conan
- C++ compiler supported C++20 (optional)

### Creating package

```shell
conan export . ext/0.1.2@_/_
conan install ext/0.1.2@_/_ --build=ext --profile=gcc
conan test test_package ext/0.1.2@_/_ --profile=gcc
```

### Uploading package

```shell
conan upload ext/0.1.2@_/_ --all -r isnullxbh/public-conan
```

## Contact

Oleg E. Vorobiov <isnullxbh@gmail.com>
