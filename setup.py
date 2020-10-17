#!/usr/bin/python

import setuptools

with open("./kodi_remotecontrol/__init__.py", "r") as fh:
    for line in fh.read().splitlines():
        if line.startswith('__version__'):
            VERSION = line.split('"')[1]
            
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
KEYWORDS = ('kodi api remote control')

setuptools.setup(
    name="kodi_remotecontrol",
    version=VERSION,
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    description="Python remote control gateway for Kodi server",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dmachard/kodi_remotecontrol",
    packages=['kodi_remotecontrol'],
    include_package_data=True,
    platforms='any',
    keywords=KEYWORDS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    entry_points={'console_scripts': ['kodi_remotecontrol = kodi_remotecontrol.gateway:start_remotecontrol']},
    install_requires=[
        "websockets",
        "requests"
    ]
)
