#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-05-28 16:24 

# @Author : liumengjia

# @File : test_smtpsimple.py 

# @Software: PyCharm

import pytest

@pytest.fixture()
def smtp_connection():
    import smtplib
    connection = smtplib.SMTP_SSL('smtp.126.com',465,timeout=4)
    yield connection
    print('teardown smtp')
    connection.close()

def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250
    assert 0

