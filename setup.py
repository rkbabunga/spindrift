# Copyright 2017-2024, Ryan P. Kelly.

from setuptools import setup


setup(
    name="spindrift",
    version="5.4",
    description="package python applications for AWS Lambda, AWS Elastic Beanstalk, AWS Batch (Docker)",
    author="Ryan P. Kelly",
    author_email="ryan@ryankelly.us",
    url="https://github.com/f0rk/spindrift",
    install_requires=[
        "pip",
        "pyyaml",
        "requests",
        "werkzeug",
    ],
    tests_require=[
        "pytest",
    ],
    package_dir={"": "lib"},
    packages=["spindrift"],
    scripts=["tools/spindrift"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
    ],
)
