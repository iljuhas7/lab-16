#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from . import struct


def save(file_name: str, items: list):
    with open(file_name, "w", encoding="utf-8") as TextIO:
        list_item = []
        for item in items:
            list_item.append(item.to_word())

        json.dump(list_item, TextIO, ensure_ascii=False, indent=4)


def load(file_name: str):
    with open(file_name, "r", encoding="utf-8") as fin:
        res = json.load(fin)
        list_item = []

        for item in res:
            list_item.append(
                struct.Item(
                    item["name"],
                    item["post"],
                    item["year"]
                )
            )

        return list_item
