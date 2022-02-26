from setuptools import setup, find_packages

setup(
    name="repo_a",
    version="0.0.1",
    install_requires=["repo_b", "repo_c", "pymongo"],
    packages=find_packages("."),
)
