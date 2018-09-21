from os.path import dirname, join

from setuptools import find_packages, setup

setup(
    name="boltun",
    version="1.0.0",
    description="NLU datasets generator",
    author="meiblorn",
    license="MIT",
    url="https://github.com/meiblorn/boltun",
    packages=find_packages(),
    long_description=open(join(dirname(__file__), "README.md")).read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
