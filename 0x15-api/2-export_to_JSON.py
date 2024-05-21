#!/usr/bin/python3
""" This script uses a REST api to store information about
all tasks that are owned by an employee in a json file"""


import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_res = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(employee_id))

    employee = employee_res.json()

    employee_name = employee.get('username')

    params = {'userId': employee_id}
    todos_res = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=params)
    total_tasks = todos_res.json()

    dct = {'{}'.format(employee_id): []}

    for task in total_tasks:
        dct.get('{}'.format(employee_id)).append(
            {"task": task.get('title'), "completed": task.get('completed'),
             "username": employee_name})
    json_string = json.dumps(dct)
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json_file.write(json_string)
