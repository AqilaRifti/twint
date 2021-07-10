import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Package info
package = {
    "name": "nvn",
    "version": "1.0.0",
    "description": "twint NexT Gen Project Manager",
    "github_url": "https://github.com/musangtara/nvn"
}


setup(
    name=package["name"],
    version=package["version"],
    description=package["description"],
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ardustri/Externatus/eternatus",
    author="Ardustri",
    author_email="info@nvn.sh",
    license="MPL-2.0-or-later",
    classifiers=[
        "License :: OSI Approved",
        "Programming Language :: Python :: 3",
    ],
    packages=["x5"],
    include_package_data=True,
    install_requires=["colorama"],
    entry_points={
        "console_scripts": [
            "nvn=nvn.__main__:main",
        ]
    },
)
