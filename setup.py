# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cpce/__init__.py
from cpce import __version__ as version

setup(
	name='cpce',
	version=version,
	description='Customizations for CPCE',
	author='Gregor Mogeritsch',
	author_email='gregor.mogeritsch@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
