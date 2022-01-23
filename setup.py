from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in descriptive/__init__.py
from descriptive import __version__ as version

setup(
	name="descriptive",
	version=version,
	description="custom app",
	author="k2s.co",
	author_email="info@k2s.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
