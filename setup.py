from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in cleantheme/__init__.py
from cleantheme import __version__ as version

setup(
	name='cleantheme',
	version=version,
	description='Clean Theme for ERPNext Frontend',
	author='@LarryDevops',
	author_email='larrydevops@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
