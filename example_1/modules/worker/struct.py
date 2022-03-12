#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


class Item:
    name: str = None
    post: str = None
    year: int = None

    def __init__(self, name: str = None, post: str = None, year: int = 0):
        self.name = name
        self.post = post
        self.year = year

    def to_word(self):
        return {
            'name': self.name,
            'post': self.post,
            'year': self.year
        }

    def __iter__(self):
        yield from {
            'name': self.name,
            'post': self.post,
            'year': self.year
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()