#!/usr/bin/python3
"""  export data in the CSV format. """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """ main code """
    print("0")
    r_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos').json()
    r_users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    print("1")
    r_user_dict = list(
        filter(
            lambda elem: elem.get('id') == int(
                argv[1]),
            r_users))[0]
    print("2")
    r_info_filtered = list(
        filter(
            lambda elem: elem.get('userId') == int(
                argv[1]),
            r_info))
    print("3")
    with open('{}.csv'.format(argv[1]), 'w') as f:
        fields = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for data in r_info_filtered:
            data['name'] = r_user_dict.get('username')
            del data['id']
            writer.writerow(data)
