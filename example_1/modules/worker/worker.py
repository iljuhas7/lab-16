#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from . import *


class Worker:
    workers = []

    def call_cmd(self, command) -> bool:
        if command == "exit":
            return False

        elif command == "add":
            self.workers.append(InputEx.create_item())

            if len(self.workers) > 1:
                self.workers.sort(key=lambda item: item.name)

        elif command == "list":
            DisplayEx.show(self.workers)

        elif command.startswith("select"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                DisplayEx.show(SelectEx.get(self.workers, int(parts[1])))
            else:
                print("[Error]: No found argument file (>>> select [date])")

        elif command.startswith("save"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                JsonEx.save(parts[1], self.workers)
            else:
                print("[Error]: No found argument file (>>> save [file])")

        elif command.startswith("load"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                self.workers = JsonEx.load(parts[1])
            else:
                print("[Error]: No found argument file (>>> load [file])")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

        return True
