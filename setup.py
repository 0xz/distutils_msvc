#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import pathlib
import platform
import shutil
import sys

import distutils
from distutils import sysconfig
from distutils.version import LooseVersion
from distutils.command.build import build
from distutils.command.clean import clean

from setuptools import find_packages, setup, Command
from setuptools.command.install import install
from setuptools.extension import Extension

include_dirs = ["./inc"]
extra_compile_args = ["-Wall", "-DDLL_EXPORT"]

class Build(build):
    def run(self):
        self.run_command('build_ext')
        build.run(self)

class Clean(clean):
    def run(self):
        shutil.rmtree("./build", ignore_errors=True)

def create_extension(name, dir, cpp_files, h_files, libs=[]):

    libraries = []
    library_dirs = []

    for lib in libs:
        n = "_"+lib["name"]
        n = n + os.path.splitext(sysconfig.get_config_var("SO"))[0]
        libraries.append(n)
        library_dirs.append(lib["dir"])

    return Extension(
        dir, 
        sources=cpp_files,
        extra_compile_args=extra_compile_args,
        extra_link_args=[],
        define_macros=[],
        swig_opts=[],
        libraries=libraries,
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        runtime_library_dirs=[],
        depends=h_files,
        language="c++"
    )

lib_a = {
    "cpp_files": ["src/a/a.cpp" ],
    "h_files": ["inc/a.hpp" ],
    "dir": "bin/build._a",
    "name": "a",
}

lib_b = {
    "cpp_files": ["src/b/b.cpp" ],
    "h_files": ["inc/b.hpp" ],
    "dir": "bin/build._b",
    "name": "b",
    "libs" : [lib_a]
}

setup(
    name="msvc_link",
    version='1',
    description="Failure scenario for msvc in distutils",
    ext_modules=[
        create_extension(**lib_a), 
        create_extension(**lib_b)
    ],
    packages=find_packages(),
    cmdclass={'build': Build, 'clean': Clean}
)
