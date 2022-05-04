#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import struct


def get_format(s: str, t1: str = None, t2: str = None, t3: str = None, t4: str = None):
    if "line" in s:
        return '+-{}-+-{}-+-{}-+-{}-+'.format('-' * 4, '-' * 30, '-' * 20, '-' * 8)

    if "text" in s:
        return '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(t1, t2, t3, t4)


def show(items: list):
    if items:
        print(get_format("line"))
        print(get_format("text", "№", "Ф.И.О.", "Должность", "Год"))
        print(get_format("line"))

        for idx, item in enumerate(items, 1):
            if isinstance(item, struct.Item):
                print(get_format("text", str(idx), item.name, item.post, item.year))

        print(get_format("line"))

    else:
        print("Список работников пуст.")
