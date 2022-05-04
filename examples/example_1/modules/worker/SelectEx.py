#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date


def get(items, period):
    today = date.today()
    result = []

    for item in items:
        if today.year - item.year >= period:
            result.append(item)

    return result
