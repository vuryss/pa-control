#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='PA Control Script',
    version='1.0',
    packages=find_packages('src'),
    package_dir={"": "src"},
    # py_modules=['pa_control'],
    install_requires=[
        'click', 'pulsectl'
    ],
    entry_points={
        'console_scripts': [
            'pa-control = pa_control:main'
        ]
    },
    include_package_data=True,
    author='Georgi Georgiev',
    author_email='vuryss@gmail.com',
    description='Python script for sane multi-sink volume control that you can bind to keyboard.',
)
