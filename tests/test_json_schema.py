#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-06-03 16:18 

# @Author : liumengjia

# @File : test_json_schema.py 

# @Software: PyCharm

from jsonschema import validators

def test_json_schema_validator():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "data": {
                "type": "object",
                "properties": {
                    "cur_num": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 10,
                        "exclusiveMaximum": False
                    },
                    "keyword": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 10
                    },
                    "vip": {
                        "type": "boolean"
                    },
                    "list": {
                        "type": "array",
                        "minItems": 1,
                        "maxItems": 10,
                        "items": {
                            "type": "object",
                            "properties": {
                                "album_id": {
                                    "type": "integer"
                                },
                                "publish": {
                                    "type": "string",
                                    "format": "date-time"
                                }
                            },
                            "required": [
                                "album_id",
                                "publish"
                            ]
                        }
                    }
                },
                "required": [
                    "cur_num",
                    "keyword",
                    "vip",
                    "list"
                ]
            }
        },
        "required": [
            "data"
        ]
    }
    respose_data = {
        "data": {
            "cur_num": 20,
            "keyword": "朴树",
            "vip": True,
            "list": [
                {
                    "album_id": 2032482,
                    "publish": "2018-11-13T20:20:39+00:00"
                },
                {
                    "album_id": 7986,
                    "publish": "2018-11-13T20:20:39+00:00"
                }
            ]
        }
    }
    va = validators.Draft4Validator(schema)
    va.validate(respose_data)
