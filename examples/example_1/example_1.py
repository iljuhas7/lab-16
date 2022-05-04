#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from modules.worker import worker as w

worker = w.Worker()


def main():
    while worker.call_cmd(input(">>> ").lower()):
        pass


if __name__ == '__main__':
    main()
