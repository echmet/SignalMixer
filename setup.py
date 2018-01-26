#setup.py
import sys, os
from cx_Freeze import setup, Executable

__version__ = "0.0.1"

packages = ["ui", "forms", "os", "qwt", "PyQt5", "guiqwt", "numpy"]

setup(
    name = "SigMix",
    description='ECHMET Signal mixer',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': [],
    'excludes': ["tkinter"],
    'include_msvcr': True,
}},
executables = [Executable("themixer.py",base="Win32GUI")]
)
