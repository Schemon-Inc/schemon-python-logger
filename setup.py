from setuptools import setup, find_packages

import subprocess

VERSION = "0.0.2"


def create_git_tag(version):
    try:
        subprocess.check_call(["git", "tag", f"v{version}"])
        subprocess.check_call(["git", "push", "origin", f"v{version}"])
    except subprocess.CalledProcessError as e:
        print(f"Error creating or pushing tag: {e}")


create_git_tag(VERSION)

setup(
    name="schemon-python-logger",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="Apache License 2.0",
    license_files=["LICENSE"],  # Specify the license file
    install_requires=[],
    entry_points={},
    include_package_data=True,  # Include package data specified in MANIFEST.in
    package_data={},
    exclude_package_data={},
)
