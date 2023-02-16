from setuptools import setup

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

with open("README.md") as f:
    long_description = f.read()

setup(
    name="colab_data_utils",
    version="0.1",
    description="Utilities for data visualization and labeling in colab",
    url="https://github.com/zzsi/colab_utils",
    author="",
    author_email="",
    license="Apache 2.0",
    packages=["colab_data_utils"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
)
