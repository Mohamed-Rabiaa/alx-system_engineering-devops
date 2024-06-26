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

    employee_name = employee.get('name')

    params = {'userId': employee_id}
    todos_res = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params=params)
    total_tasks = todos_res.json()
    completed_tasks = []
    for task in total_tasks:
        if task.get('completed'):
            completed_tasks.append(task.get('title'))

    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(total_tasks)

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, number_of_done_tasks,
                  total_number_of_tasks))

    for task in completed_tasks:
        print('\t ' + task)
