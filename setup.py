#!/usr/bin/env python3
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jinjarender",
    version="0.1",
    author="Tomas Bayer",
    author_email="tomas.bayer@gmail.com",
    description="render jinja template with data from STDIN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #packages=setuptools.find_packages(),
    scripts=['bin/jinjarender'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyyaml",
        "jinja2"
    ]
)
