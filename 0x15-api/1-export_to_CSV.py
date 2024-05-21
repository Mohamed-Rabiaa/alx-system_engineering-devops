#!/usr/bin/python3
""" This script uses a REST api to return information
about an employee TODO list progress using his ID """


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

    with open('{}.csv'.format(employee_id), 'w') as csv_file:
        for task in total_tasks:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                employee_id, employee_name, task.get('completed'),
                task.get('title')))
