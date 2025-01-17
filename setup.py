# -*- coding: utf-8 -*-

"""Anaconda Client setup script."""

import os
import setuptools


root = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(root, 'requirements.txt'), 'rt', encoding='utf-8') as stream:
    install_requires = list(filter(bool, (
        requirement.split('#', 1)[0].strip() for requirement in stream
    )))

with open(os.path.join(root, 'requirements-extra.txt'), 'rt', encoding='utf-8') as stream:
    extras_require = list(filter(bool, (
        requirement.split('#', 1)[0].strip() for requirement in stream
    )))

__about__ = {}
with open(os.path.join(root, 'binstar_client', '__about__.py'), 'rt', encoding='utf-8') as stream:
    exec(stream.read(), __about__)


setuptools.setup(
    name='anaconda-client',
    version=__about__['__version__'],
    description='Anaconda.org command line client library',
    license='BSD License',
    author='Sean Ross-Ross',
    author_email='srossross@gmail.com',
    url='https://github.com/Anaconda-Platform/anaconda-client',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],

    install_requires=install_requires,
    extras_require={
        'full': extras_require,
    },
    packages=setuptools.find_packages(include=['binstar_client', 'binstar_client.*']),
    entry_points={
        'console_scripts': [
            'anaconda = binstar_client.scripts.cli:main',
            'binstar = binstar_client.scripts.cli:main',
            'conda-server = binstar_client.scripts.cli:main',
        ],
    },
)
