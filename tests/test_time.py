#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-05-26 15:54 

# @Author : liumengjia

# @File : test_time.py 

# @Software: PyCharm

import pytest

from datetime import datetime,timedelta

testdata = [
    (datetime(2020,12,12),datetime(2020,12,11),timedelta(1)),
    (datetime(2020,12,11),datetime(2020,12,12),timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected",testdata)
def test_time_distance_v0(a,b,expected):
    diff = a -b
    assert diff == expected