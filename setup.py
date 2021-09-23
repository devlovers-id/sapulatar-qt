#!/usr/bin/env python3

import os
import io
import shutil
import sys

from distutils.command.install_data import install_data
from setuptools import setup, find_packages
from setuptools.command.install import install

# minimal python version check
v = sys.version_info
if v[0] >= 3 and v[:2] < (3, 8):
    error = "ERROR: Sapulatar requires python version 3.8 and above"
    print(error, file=sys.stderr)
    sys.exit(1)

from sapulatar_qt import __version__, __website_url__, __author__, __title__

NAME="sapulatar-qt"
LIBNAME="sapulatar_qt"

def get_subpackages(name):
    p = []
    for root, _dirname, _filename in os.walk(name):
        if os.path.isfile(os.path.join(root, '__init__.py')):
            p.append('.'.join(root.split(os.sep)))
    return p

def get_packages():
    packages = get_subpackages(LIBNAME)
    return packages

def get_data_files():
    """
    Return data_files in a platform dependent manner.
    """
    if sys.platform.startswith('linux'):
        data_files = [('share/applications', ['assets/sapulatar-qt.desktop']),
                      ('share/icons', ['assets/sapulatar-qt.png']),
                     ]
    elif os.name == 'nt':
        # TODO add windows stuffs here
        data_files = []
    else:
        data_files = []

    return data_files


# =============================================================================
# Make Linux detect Citramanik desktop file (will not work with wheels)
# =============================================================================
class CustomInstallData(install_data):
    def run(self):
        install_data.run(self)
        if sys.platform.startswith('linux'):
            try:
                subprocess.call(['update-desktop-database'])
            except:
                print("ERROR: unable to update desktop database",
                      file=sys.stderr)


CMDCLASS = {'install_data': CustomInstallData}

# long description from readme.md
with io.open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

#=================
# Setup Arguments
#=================
setup_args = dict(
    name=NAME,
    version=__version__,
    platforms=["Windows", "Linux", "Mac OS-X"],
    python_requires='>=3.8',
    packages=get_packages(),
    data_files=get_data_files(),
    package_data={'sapulatar_qt': ['ui/assets/*.png']},
    url=__website_url__,
    license="GPL-3.0",
    author=__author__,
    author_email="support@dev-is.my.id",
    description="Simple tool to help you remove background from your images/photos.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    cmdclass=CMDCLASS
)

install_requires = [
    "PySide2==5.15.2",
]

setup_args['install_requires'] = install_requires
setup_args['entry_points'] = {
        'gui_scripts': [
                'sapulatar-qt = sapulatar_qt.main:main'
            ]
        }

#======================
# Main Setup execution
#======================
setup(**setup_args)
