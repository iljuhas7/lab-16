#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from . import struct


def create_item():
    item = struct.Item()
    item.name = input("Фамилия и инициалы? ")
    item.post = input("Должность? ")
    item.year = int(input("Год поступления? "))

    return item
