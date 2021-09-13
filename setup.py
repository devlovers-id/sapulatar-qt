#!/usr/bin/env python3

import os
import shutil
import sys

from distutils.command.install_data import install_data
from setuptools import setup, find_packages
from setuptools.command.install import install

from sapulatar import __version__, __website_url__, __author__, __title__

# Clear previous build
if os.path.isdir("dist"):
    shutil.rmtree("dist")
if os.path.isdir("build"):
    shutil.rmtree("build")

NAME="sapulatar-qt"
LIBNAME="sapulatar"

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
        data_files = [('share/applications', ['scripts/sapulatar-qt.desktop']),
                      ('share/icons/', ['icons/linux/sapulatar-qt.png']),
                      ('share/metainfo',
                       ['scripts/id.devlovers.sapulatar.appdata.xml'])]
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


# =============================================================================
# Main scripts
# =============================================================================
# NOTE: the '[...]_win_post_install.py' script is installed even on non-Windows
# platforms due to a bug in pip installation process
# See spyder-ide/spyder#1158.

#SCRIPTS = ['%s_win_post_install.py' % NAME]
SCRIPTS = []
SCRIPTS.append('sapulatar')

#if os.name == 'nt':
#    SCRIPTS += ['sapulatar.bat']


#=================
# Setup Arguments
#=================
setup_args = dict(
    name=NAME,
    version=__version__,
    scripts=[os.path.join('scripts', fname) for fname in SCRIPTS],
    platforms=["Windows", "Linux", "Mac OS-X"],
    python_requires='>=3.8',
    packages=get_packages(),
    data_files=get_data_files(),
    url=__website_url__,
    license="GPL-3.0",
    author=__author__,
    author_email="support@dev-is.my.id",
    description="Simple tool to help you remove background from your images/photos.",
    cmdclass=CMDCLASS
)

install_requires = [
    "PySide2==5.15.2",
]

setup_args['install_requires'] = install_requires
setup_args['entry_points'] = {
        'gui_scripts': [
                'sapulatar-qt = sapulatar.main:main'
            ]
        }
setup_args.pop('scripts', None)
#======================
# Main Setup execution
#======================
setup(**setup_args)
