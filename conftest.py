#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-05-31 23:17 

# @Author : liumengjia

# @File : conftest.py 

# @Software: PyCharm

import inspect
import os
import re
import allure
import pytest
import yaml
import logging

def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")

@pytest.fixture(scope="session")
def env(request):

    # request是pytest提供的内置的一个fixture函数，它提供了测试函数的上下文信息
    # request.config.rootdir属性，这个属性表示的是pytest.ini这个配置文件所在的目录
    # 注意：当根目录下没有pytest.ini配置文件时，会默认指向conftest.py所在目录；此时若要指向项目根目录，则在项目目录下新建一个 pytest.ini 空文件即可

    # 因为我们的测试项目中pytest.ini处于项目的根目录，所以config_path的完整路径就是：/Users/liumengjia/Documents/Project/Interface_Automation/config/test/config.yaml

    config_path = os.path.join(request.config.rootdir,
    # os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
                               "config",
                               request.config.getoption("environment"),
                               "config.yaml")
    print(config_path)
    with open(config_path) as f:
        env_config = yaml.load(f.read(),Loader=yaml.SafeLoader)
        print(env_config)
    return env_config