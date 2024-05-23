#!/usr/bin/python3
""" This script uses a REST api to store information about
all tasks that are owned by all employees in a json file"""


import json
import requests
import sys


if __name__ == "__main__":
    employee_res = requests.get('https://jsonplaceholder.typicode.com/users')
    employees = employee_res.json()
    dct = {}

    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('username')
        dct[employee_id] = []

        todos_res = requests.get('https://jsonplaceholder.typicode.com/todos')
        total_tasks = todos_res.json()

        for task in total_tasks:
            if task.get('userId') == employee_id:
                employee_tasks = {
                    "username": employee_name,
                    "task": task.get('title'),
                    "completed": task.get('completed')}
                dct.get(employee_id).append(employee_tasks)

    json_string = json.dumps(dct)
    with open('todo_all_employees.json', 'w') as json_file:
        json_file.write(json_string)
