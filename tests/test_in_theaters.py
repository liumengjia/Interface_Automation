#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-05-26 14:24 

# @Author : liumengjia

# @File : test_in_theaters.py 

# @Software: PyCharm

import pytest
import requests
import allure

from utils.commlib import get_test_data

cases,parameters = get_test_data("/Users/liumengjia/Documents/Project/Interface_Automation/data/test_in_theaters.yaml")
list_params = list(parameters)

@allure.feature("获取电影列表")  # 用feature说明产品需求，可以理解为JIRA中的Epic
class TestInTheaters():
    @allure.story("准备测试数据")  # 用story说明用户场景，可以理解为JIRA中的Story
    @pytest.fixture(scope="function")
    def preparation(self):
        print("在数据库中准备测试数据")
        test_data = "在数据库中准备测试数据"
        yield test_data
        print("清理测试数据")

    @allure.story("获取电影列表") # 用story说明用户场景，可以理解为JIRA中的Story
    @pytest.mark.parametrize("case,http,expected",list_params, ids=cases)
    def test_in_theaters(self, env,case, http, expected,preparation):

        r = requests.request(http["method"],
                             url=env["host"]["douban"]+http["path"],
                             params=http["params"])
        if r.content:
            response = r.json()

            assert response["count"] == expected['response']["count"]
            assert response["start"] == expected['response']["start"]
            assert response["title"] == expected['response']["title"], "实际的标题是：{}".format(response["title"])
