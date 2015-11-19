from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
	long_description = f.read()

setup(
	name='winrm-client',
	version='0.1.0',

	description='A convenient interface to WinRM using WSMan',
	long_description=long_description,

	url='https://github.com/invliD/python-winrm-client',

	author='invliD',
	author_email='pypi@invlid.com',

	license='Apache License 2.0',

	classifiers=[
		'Development Status :: 3 - Alpha',

		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',

		'License :: OSI Approved :: Apache Software License',

		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
	],

	keywords='winrm monitoring wsman',

	packages=['winrm'],

	install_requires=[
		'pywsman',
	],
)
