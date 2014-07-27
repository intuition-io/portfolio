# -*- coding: utf-8 -*-
# vim:fenc=utf-8

'''
  :copyright (c) 2014 Xavier Bruhiere
  :license: Apache 2.0, see LICENSE for more details.
'''

import multiprocessing
import setuptools
from portfolio import (
    __version__, __author__, __licence__, __project__, __teaser__
)

REQUIREMENTS = [
    'numpy',
    'pandas',
    'scipy'
]


def long_description():
    ''' Safely read README.md '''
    try:
        with open('README.md') as fd:
            return fd.read()
    except IOError:
        return "failed to read README.md"


setuptools.setup(
    name=__project__,
    version=__version__,
    description=__teaser__,
    author=__author__,
    author_email='xavier.bruhiere@gmail.com',
    packages=setuptools.find_packages(),
    long_description=long_description(),
    license=__licence__,
    install_requires=REQUIREMENTS,
    url="https://github.com/intuition-io/portfolio",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: System :: Distributed Computing',
    ]
)
