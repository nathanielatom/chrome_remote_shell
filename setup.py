from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

requirements = []

setup(
    name='chrome_remote_shell',
    version='1.2',
    description='Client for talking to the Google Chrome remote shell port',
    long_description=long_description,
    author='Fred Clift and Brandon Craig Rhodes',
    author_email='fred@clift.org',
    url='https://github.com/minektur/chrome_remote_shell',
    packages=find_packages(path),
    platforms='any',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        ],
    install_requires=['websocket-client'],
    )
