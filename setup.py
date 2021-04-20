from setuptools import setup, find_packages

base_packages = []

test_packages = [
    "pytest>=6.2.3",
    "black>=20.8b1",
    "flake8>=3.9.1",
]

util_packages = [
    "pre-commit>=2.12.1",
]

dev_packages = test_packages + util_packages

setup(
    name="cypher",
    version="0.0.1",
    packages=find_packages(),
    extra_require={"dev": dev_packages, "test": test_packages},
)
