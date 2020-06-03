#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-06-03 13:24 

# @Author : liumengjia

# @File : test_marks.py 

# @Software: PyCharm

import sys
import pytest

class TestMarks():

    @pytest.mark.skip(reason="not implememtation")
    def test_the_unknown(self):
        """
        跳过不执行，未实现
        :return:
        """
        assert 0

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
    def test_skip(self):
        """
        低于Python3.7版本不执行此条测试用例
        :return:
        """
        assert 1

    @pytest.mark.xfail
    def test_xfail(self):
        """
        Indicate that you expect it to fail
        这条用例执行失败时，测试结果被标记为xfail(expected to fail)，并且不打印错误信息。
        这条用例执行成功时，测试结果被标记为xpassed(unexpectedly passing)
        :return:
        """
        assert 0

    @pytest.mark.xfail(run=False)
    def test_xfail_not_run(self):
        """
        run=False，表示这条用例不执行
        :return:
        """

    @pytest.mark.slow
    def test_slow(self):
        """
        自定义标签
        :return:
        """
        assert 0