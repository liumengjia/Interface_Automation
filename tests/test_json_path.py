#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-06-03 16:11 

# @Author : liumengjia

# @File : test_json_path.py 

# @Software: PyCharm

import jsonpath

response = {"store": {
    "book": [
        {"category": "reference",
         "author": "Nigel Rees",
         "title": "Sayings of the Century",
         "price": 8.95
         },
        {"category": "fiction",
         "author": "Evelyn Waugh",
         "title": "Sword of Honour",
         "price": 12.99
         },
        {"category": "fiction",
         "author": "Herman Melville",
         "title": "Moby Dick",
         "isbn": "0-553-21311-3",
         "price": 8.99
         },
        {"category": "fiction",
         "author": "J. R. R. Tolkien",
         "title": "The Lord of the Rings",
         "isbn": "0-395-19395-8",
         "price": 22.99
         }
    ],
    "bicycle": {
        "color": "red",
        "price": 19.95
    }
}
}


def test_authors():
    """
    '$.store.book[*].author'表示store节点下book结点下所有对象的author值
    """
    author_list = jsonpath.jsonpath(response, '$.store.book[*].author')
    assert author_list == ['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']


def test_all_goods():
    """'$.store.*'，表示根节点$下store属性下的所有对象，没写"""
    category_dx = jsonpath.jsonpath(response, '$.store.*')
    print(category_dx)


def test_all_price():
    """'$.store..price' 表示根节点的store属性下，递归查找price属性的值
    '$..price' 表示根节点下，递归查找price属性的值"""
    store_price_list = jsonpath.jsonpath(response, '$.store..price')
    assert store_price_list == [8.95, 12.99, 8.99, 22.99, 19.95]


def test_third_book():
    """
    '$..book[2]'表示根节点下递归查找所有book属性中第3个对象，

    """
    book_3 = jsonpath.jsonpath(response, '$.store.book[2]')
    assert book_3[0]['title'] == "Moby Dick!"


def test_last_book_isbn():
    last_book_isbn = jsonpath.jsonpath(response, f'$.store.book[-1:].isbn')
    # last_book_isbn = jsonpath.jsonpath(response, f'$.store.book[(@.length-1)].isbn')
    assert last_book_isbn == "1-395-19395-8"


def test_12_books_price():
    """
    '$..book[0,1]'表示根节点下递归查找所有的book属性值的第0个和第1个元素，
    """
    book_12 = jsonpath.jsonpath(response, '$..book[0,1].price')
    assert book_12[0] + book_12[1] == 8.95 + 12.99


def test_slice_with_step():
    """"""
    prices = jsonpath.jsonpath(response, '$..book[::2].price')
    for price in [8.95, 8.99]:
        assert price in prices


def test_2books_cheap_than_10():
    """
    '$..book[?(@.price<10)]'表示根节点下book属性的所有price小于10的元素
    """
    book_lg10 = jsonpath.jsonpath(response, '$..book[?(@.price<10)]')
    assert len(book_lg10) <= 2


def test_has_color():
    """
    '$..[?(@.color)]'表示根节点下具有color属性的对象
    """
    colorful_goods = jsonpath.jsonpath(response, '$.store..[?(@.color)]')
    assert "green" == colorful_goods[0]['color']
