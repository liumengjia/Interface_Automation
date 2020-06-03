#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-06-03 15:04 

# @Author : liumengjia

# @File : test_assertions.py 

# @Software: PyCharm

import pytest

class TestStringAssertions():
    def  test_string_1(self):
        assert "spam" == "eggs"

    def test_string_2(self):
        assert "foo 1 bar" == "foo 2 bar"

    def test_string_3(self):
        assert "foo\nspam\nbar" == "foo\neggs\nbar"

    def test_string_4(self):
        def func():
            return "streaming"

        assert func().startswith("S")

def test_func():
    def func():
        return [1,2,3]

    assert func() == [1,2,4]

class TestCollections():
    def test_dict(self):
        assert {"a": 0, "b": 1, "c": 0} == {"a": 0, "b": 2, "d": 0}

    def test_dict2(self):
        exp = {"a":0,"b":{"c":0}}
        act = {"a":0,"b":{"c":2}}
        assert exp == act

    def test_list(self):
        list1 = [0,1,2]
        list2 = [0,1,3]
        assert list1 == list2

    def test_list2(self):
        assert [0,1,2] == [0,1,[1,2]]

    def test_list3(self):
        assert 2 in [0,1,[1,2]]

    def test_set(self):
        assert {0,1,11,23} == {0,11,2}

def test_zero_divison():
    with pytest.raises(ZeroDivisionError) as e:
        1/0
    assert 'division by zero' in str(e.value)