#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

# Для своего варианта лабораторной работы 2.8 необходимо дополнительно реализовать
# сохранение и чтение данных из файла формата JSON. Необходимо также проследить за тем,
# чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной работы

students = []
count = 0
file_name = "inv_1.json"


def get_command():
    return input(">>> ").lower()


def is_command(is_name_command):
    for command in list_commands:
        if is_name_command == command['name']:
            return True

    return False


def call_command(in_name_command):
    for command in list_commands:
        if in_name_command == command['name']:
            return command['fun']()

    return False


def student_add():
    name = input("Фамилия и инициалы? ")
    number = input("Номер группы? ")
    z = str(input("Успеваемость? "))

    student = {
        'name': name,
        'number': number,
        'z': z,
    }

    students.append(student)
    if len(student) > 1:
        students.sort(key=lambda item: item.get('name', ''))


def student_print_line():
    print('+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
    )


def student_print_list():

    student_print_line()
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Номер группы",
            "Успеваемость"
        )
    )
    student_print_line()
    for idx, worker in enumerate(students, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                worker.get('name', ''),
                worker.get('number', ''),
                worker.get('z', 0)
            )
        )

    student_print_line()


def student_print_select():
    cn = 0
    for student in students:
        if "2" in student.get('z', ''):
            cn -= 1
            print(
                '{:>4} {}'.format('*', student.get('name', '')),
                '{:>1} {}'.format('группа №', student.get('number', ''))
            )
    if cn == 0:
        print('Таких студентов нет')


def help_print_list():
    print("Список команд:")
    print("\texit - завершить работу с программой;")
    for command in list_commands:
        print(f"\t{command['name']} - {command['desc']};")


def student_save():
    with open(file_name, "w", encoding="utf-8") as TextIO:
        list_item = []
        for item in students:
            list_item.append(
                {
                    'name': item["name"],
                    'number': item["number"],
                    'z': item["z"]
                }
            )

        json.dump(list_item, TextIO, ensure_ascii=False, indent=4)


def student_load():
    global students
    
    with open(file_name, "r", encoding="utf-8") as fin:
        res = json.load(fin)
        students = []

        for item in res:
            student = {
                'name': item["name"],
                'number': item["number"],
                'z': item["z"],
            }
            
            students.append(student)
            if len(student) > 1:
                students.sort(key=lambda item: item.get('name', ''))

list_commands = (
        {'name': 'help', 'fun': help_print_list, 'desc': 'добавить студента'},
        {'name': 'add', 'fun': student_add, 'desc': 'вывести список студентов'},
        {'name': 'select', 'fun': student_print_select, 'desc': 'вывести список студентов, имеющих оценку 2'},
        {'name': 'list', 'fun': student_print_list, 'desc': 'отобразить справку'},
        {'name': 'save', 'fun': student_save, 'desc': 'сохранить'},
        {'name': 'load', 'fun': student_load, 'desc': 'загрузить'}
)

def main():
    while True:
        command = get_command()

        if command == "exit":
            break

        if command:
            if is_command(command):
                call_command(command)

            else:
                print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()