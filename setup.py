import os
from setuptools import setup, find_packages
import warnings

setup(
    name='aws-tagger',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'boto3>=1.4.1',
        'botocore>=1.4.77',
        'click>=6.6',
        'docutils>=0.12',
        'futures>=3.0.5',
        'jmespath>=0.9.0',
        'python-dateutil>=2.6.0',
        'retrying>=1.3.3',
        's3transfer>=0.1.9',
        'six>=1.10.0'
    ],
    entry_points={
        "console_scripts": [
            "aws-tagger=tagger.cli:cli",
        ]
    },
    namespace_packages = ['tagger'],
    author="Patrick Cullen and the WaPo platform tools team",
    author_email="opensource@washingtonpost.com",
    url="https://github.com/washingtonpost/aws-tagger",
    download_url = "https://github.com/washingtonpost/aws-tagger/tarball/v0.1.0",
    keywords = ['tag', 'tagger', 'tagging', 'aws'],
    classifiers = []
)