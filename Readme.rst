Baidu Translation
=================

this is a python translation package based on baidu translation api.

**Installation**

.. code:: bash


    git clone --depth 1 https://github.com/zaiic/baidu-translate-cli.git

    cd baidu-translate-cli

    python setup.py sdist

    cd dist

    pip install baidu-translate-cli-0.2.3.tar.gz

**Installation**

.. code:: bash

    pip uninstall baidu-translate-cli

1. register a account on http://api.fanyi.baidu.com/api/trans/product/index **2000,000 characters per month is free.**
2. get appid and secretKey, write into **~/.config/baidu-trans/main.json**

**Usage**

.. code:: bash
    
    baidu-trans -h
