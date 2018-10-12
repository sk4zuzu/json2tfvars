#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

entry_points = '''
[console_scripts]
json2tfvars=json2tfvars:json2tfvars
'''

setuptools.setup(
    name="json2tfvars",
    version="0.0.1",
    author="Michal Opala",
    author_email="sk4zuzu@gmail.com",
    description="simple tfvars (HCL) converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sk4zuzu/json2tfvars",
    packages=setuptools.find_packages(),
    py_modules=[
        'json2tfvars',
    ],
    install_requires=[
        'pyhcl',
    ],
    entry_points=entry_points,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        "Operating System :: OS Independent",
    ],
)

# vim:ts=4:sw=4:et:syn=python:
