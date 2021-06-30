
# find_packages will look for folders which are having __init__.py file to make those folders a package.

from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    description="It's a Wine Quality Package",
    author="S.S.R",
    packages=find_packages(),
    license="MIT"
)
