from setuptools import setup
import setuptools
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



setup(
    name='GithubTesting',
    version='0.0.1',
    description=('Testing of actions on GitHub.'),
    long_description=long_description,
    author='Jakob Lass',
    author_email='lass.jakob@gmail.com',
    url='https://github.com/jakob-lass/GithubTesting',
    python_requires='>=3.6' ,
    install_requires=['matplotlib>=3'], 
    classifiers=[
        'Development Status :: 3 - Alpha',
          'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'],
    )
