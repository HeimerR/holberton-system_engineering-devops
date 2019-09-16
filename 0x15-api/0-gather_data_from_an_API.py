#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    """ main code """
    r_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    r_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    r_user_dict = list(
        filter(
            lambda elem: elem.get('id') == int(
                argv[1]),
            r_users))[0]
    print('Employee {} is done with '.format(r_user_dict.get('name')), end='')
    r_info_filtered = list(
        filter(
            lambda elem: elem.get('userId') == int(
                argv[1]),
            r_info))
    DONE_TASKS = list(
        filter(
            lambda elem: elem.get('completed'),
            r_info_filtered))
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    TOTAL_NUMBER_OF_TASKS = len(r_info_filtered)
    print('tasks({}/{}):'.format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in DONE_TASKS:
        print('\t {}'.format(i.get('title')))
