from setuptools import setup, find_packages

setup(
    name="data-structures-algos-python",
    version="0.0.1",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pytest==3.6.2",

    ]
)
