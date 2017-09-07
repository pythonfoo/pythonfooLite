#! /usr/bin/env python3
# partly taken from https://github.com/pypa/sampleproject/blob/02130aeda025ca86975258f953b5d2531d74e94c/setup.py

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README')) as f:
    long_description = f.read()

setup(
    name='pythonfoo-hello-world',

    # Versions should comply with PEP440.
    version='0.1.0',

    description='displays "Hello World!"',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pythonfoo/pythonfooLite/tree/master/Level_11',

    # Author details
    author='Pythonfoo',
    author_email='pythonfoo@chaosdorf.de',

    # Choose your license
    license='WTFPL',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        
        # Where does it run?
        'Environment :: Console',
        
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        
        # Language
        'Natural Language :: English',
        
        # Topic
        'Topic :: Utilities',
        'Topic :: Internet',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='hello-world',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['pythonfoo_hello_world'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed.
    install_requires=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'phw=pythonfoo_hello_world:run',
        ],
    },
)
