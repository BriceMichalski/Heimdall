"""The setup script."""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Brice Michalski",
    author_email="brice.michalski.92@gmail.com",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="heimdall",
    packages=find_packages(include=["heimdall"]),
    url="https://github.com/BriceMichalski/Heimdall",
    version="0.1.0",
    zip_safe=False,
    entry_points={"console_scripts": ["heimdall=heimdall.cli:main"]},
)