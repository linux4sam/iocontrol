#
# I/O Control Application
#
# Copyright (C) 2017 Microchip Technology Inc.  All rights reserved.
# Joshua Henderson <joshua.henderson@microchip.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import codecs
import sys
import subprocess
from setuptools import setup, find_packages
from iocontrol import __version__

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except ImportError:
    with codecs.open('README.md', encoding='utf-8') as f:
        README = f.read()

setup(
    name='iocontrol',
    author='Joshua Henderson',
    author_email='joshua.henderson@microchip.com',
    version=__version__,
    packages=['iocontrol'],
    include_package_data=True,
    install_requires=[
        'mpio>=1.0'
    ],
    extras_require={
    },
    description="Graphical hardware perpheral access using MPIO",
    long_description=README,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Embedded Systems',
    ],
    entry_points={
        'gui_scripts': [
            'iocontrol = iocontrol.iocontrol:main'
        ]
    },
)
