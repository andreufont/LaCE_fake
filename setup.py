#!/usr/bin/env python

from setuptools import setup, find_packages

description = "Post-processing of hydrodynamic simulations for the LaCE emulator"
version="0.0.1"

setup(name="lace_fake",
    version=version,
    description=description,
    url="https://github.com/andreufont/LaCE_fake",
    author="Andreu Font-Ribera et al.",
    author_email="afont@ifae.es",
    packages=find_packages(),
    )
