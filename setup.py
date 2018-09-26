#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    :author:    kuangcp 
    :homepage:  https://gitee.com/gin9/baidu-trans-cli/tree/master/
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2018 kuangcp. All rights reserved
"""
import codecs
import baidu_trans_cli
import setuptools.command.test

# -*- Long Description -*-
def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
    except IOError:
        return 'Long description error: Missing README.md file'


setuptools.setup(
    name='baidu-trans-cli',
    version='0.0.8',
    description='use baidu translation api in terminal',
    long_description=long_description(),
    keywords='translation',
    author='gin9',
    author_email='kuangcp@aliyun.com',
    url='https://gitee.com/gin9/baidu-trans-cli/tree/master/',
    license='MIT License',
    platforms=['any'],
    install_requires = ['fire>=0.1.3', 'requests>=2.19.1', 'urllib3>=1.23'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Topic :: Utilities',
        'Topic :: Terminals',
        "Topic :: System :: Distributed Computing",

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=setuptools.find_packages(exclude=['tests']),
    include_package_data=True,
    package_data={
        '': ['*.py']
    },
    entry_points={
        'console_scripts': [
            'baidu-trans = baidu_trans_cli:main',
        ],
    },
)
