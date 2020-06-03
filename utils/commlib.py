#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-05-26 16:10 

# @Author : liumengjia

# @File : commlib.py.py 

# @Software: PyCharm

import yaml

def get_test_data(test_data_path):
    case = []  # 存放测试用例名称
    http = []  # 存放请求对象
    expected = []  # 存放预期结果

    with open(test_data_path) as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
        test = data['tests']
        for td in test:
            case.append(td.get('case',''))
            http.append(td.get('http',{}))
            expected.append(td.get('expected',{}))

    parameters = zip(case,http,expected)
    return case,parameters