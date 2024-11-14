from setuptools import setup, find_packages


VERSION = "0.0.11"


setup(
    name="schemon-python-logger",
    version=VERSION,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    license="Apache License 2.0",
    license_files=["LICENSE"],  # Specify the license file
    install_requires=[
        "pyspark==3.5.0",
    ],
    entry_points={},
    python_requires=">=3.9",
    include_package_data=True,  # Include package data specified in MANIFEST.in
    package_data={},
    exclude_package_data={},
)
