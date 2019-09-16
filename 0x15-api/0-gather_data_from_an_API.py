#!/usr/bin/python3
""" given employee ID, returns information about his/her TODO list progress """
import requests
from sys import argv


if __name__ == "__main__":
    """ main code """
    r_info = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    r_users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    r_user_dict = list(
        filter(
            lambda elem: elem.get("id") == int(
                argv[1]),
            r_users))[0]
    user = r_user_dict.get('name')
    r_info_filtered = list(
        filter(
            lambda elem: elem.get('userId') == int(
                argv[1]),
            r_info))
    done = list(
        filter(
            lambda elem: elem.get('completed'),
            r_info_filtered))
    num_task = len(done)
    total_num_task = len(r_info_filtered)
    print("Employee {} is done with ".format(user), end='')
    print('tasks({}/{}):'.format(num_task, total_num_task))
    for i in done:
        print('\t {}'.format(i.get('title')))
