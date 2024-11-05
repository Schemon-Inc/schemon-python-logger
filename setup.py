from setuptools import setup, find_packages

import subprocess

VERSION = "0.0.6"


setup(
    name="schemon-python-logger",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="Apache License 2.0",
    license_files=["LICENSE"],  # Specify the license file
    install_requires=[],
    entry_points={},
    python_requires=">=3.8",
    include_package_data=True,  # Include package data specified in MANIFEST.in
    package_data={},
    exclude_package_data={},
)
