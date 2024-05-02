import io
import os
from setuptools import setup

def getRequirements(file="requirements.txt"):
    requirements = []
    with open(file) as f:
        requirements = [x for x in f.read().split("\n")]
    f.close()
    return requirements

# Use the README.md content for the long description:
with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()


setup(
    name='PyMacAuto',
    version=version,
    url='https://github.com/Existance29/pymacauto',
    author='Existance',
    author_email='',
    description=('PyMacAuto is a wrapper for several automation libraries and custom functions to create a all-in-one library for complex macros on the mac platform'),
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['pymacauto'],
    test_suite='tests',
    install_requires=getRequirements(),
    keywords="mac macro automation automate keyboard mouse cursor click press keystroke control ocr textrecognition imagedetection screenshot",
    classifiers=[
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Topic :: Utilities",
    ],
)
