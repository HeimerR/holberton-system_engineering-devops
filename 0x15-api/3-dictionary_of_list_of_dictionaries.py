#!/usr/bin/python3
"""  export data in the JSON format. for all users """
import json
import requests


if __name__ == '__main__':
    """ main code """
    r_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos')
    r_users = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    data = {}
    """ print(r_info.json()) """
    for user in r_users.json():
        todos = list(
            filter(
                lambda i: i.get('userId') == user.get('id'),
                r_info.json()))
        list_dict = []
        for dictionary in todos:
            new_dict = {}
            new_dict['task'] = dictionary['title']
            new_dict['completed'] = dictionary['completed']
            new_dict['username'] = user.get('username')
            list_dict.append(new_dict)
        data[user.get('id')] = list_dict
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
