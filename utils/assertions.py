#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-06-03 14:59 

# @Author : liumengjia

# @File : assertions.py 

# @Software: PyCharm

def assertion(exp,act):
    assert exp == act, "Expectaion is {},actual result is {}".format(exp,act)