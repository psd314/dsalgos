import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsalgos",
    version="0.0.1",
    author="Philippe Dixon",
    author_email="philippedixon@protonmail.com",
    description="Implementation of basic algorithms and data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/psd314/dsalgos",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
