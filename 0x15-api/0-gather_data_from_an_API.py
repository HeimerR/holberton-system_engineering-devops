#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress """
from sys import argv
import requests


if __name__ == '__main__':
    """ main code """
    params = {'userId': argv[1]}
    r_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos/',
        params=params)
    r_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    print('Employee {} is done with'.format(r_user.json().get('name')), end='')
    r_info_filtered = list(
        filter(
            lambda elem: elem.get('userId') == int(
                argv[1]),
            r_info.json()))
    DONE_TASKS = list(
        filter(
            lambda elem: elem.get('completed'),
            r_info_filtered))
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(r_info_filtered)
    print('tasks({}/{})'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in DONE_TASKS:
        print('\t{}'.format(i.get('title')))
