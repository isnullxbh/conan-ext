# conan-ext

A Conan recipe for the ext library

## Getting started

### Prerequisites

- Python 3
- Conan
- C++ compiler supported C++20 (optional)

### Creating package

```shell
conan export . ext/0.1.2@isnullxbh/testing
conan install ext/0.1.2@isnullxbh/testing --build=ext --profile=gcc
conan test test_package ext/0.1.2@isnullxbh/testing --profile=gcc
```

### Uploading package

```shell
conan upload ext/0.1.2@isnullxbh/testing --all -r isnullxbh/public-conan
```

## Contact

Oleg E. Vorobiov <isnullxbh@gmail.com>
