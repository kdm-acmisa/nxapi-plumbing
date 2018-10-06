from setuptools import setup
from setuptools import find_packages
import os
import re


requirements = ["requests>=2.7.0", "future", "scp"]

with open("README.md", "r") as fs:
    long_description = fs.read()


def find_version(*file_paths):
    """
    This pattern was modeled on a method from the Python Packaging User Guide:
        https://packaging.python.org/en/latest/single_source_version.html

    We read instead of importing so we don't get import errors if our code
    imports from dependencies listed in install_requires.
    """
    base_module_file = os.path.join(*file_paths)
    with open(base_module_file) as f:
        base_module_data = f.read()
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", base_module_data, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="pynxos",
    version=find_version("pynxos", "__init__.py"),
    description="A library for managing Cisco NX-OS devices through NX-API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ktbyers/pynxos",
    author="Kirk Byers; Matt Schwenn; mzbenami",
    author_email="ktbyers@twb-tech.com",
    license="Apache2",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(exclude=("test*",)),
    install_requires=requirements,
)
