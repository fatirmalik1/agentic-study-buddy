from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="LLMOPS-3",
    version="0.2",
    author="Fatir Malik",
    packages=find_packages(),
    install_requires = requirements,
)