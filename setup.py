#!/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="python-modemmanager",
      version="0.1",
      author="Judah Rand",
      author_email="JudahRand+ModemManager@gmail.com",
      description="Easy communication with ModemManager",
      url="http://github.com/JudahRand/python-modemmanager",
      license="MIT",
      packages=["ModemManager", "ModemManager.Modem"],
      install_requires=["pydbus", "datetime"],
      classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Networking",
      ])
