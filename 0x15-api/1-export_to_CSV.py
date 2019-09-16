#!/usr/bin/python3
"""  export data in the CSV format. """
from sys import argv
import csv
import requests


if __name__ == '__main__':
    """ main code """
    params = {'userId': argv[1]}
    r_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos/',
        params=params)
    r_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    r_info_filtered = list(
        filter(
            lambda elem: elem.get('userId') == int(
                argv[1]),
            r_info.json()))
    with open('{}.csv'.format(argv[1]), 'w') as f:
        fields = ["userId", "name", "completed", "title"]
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
        for data in r_info_filtered:
            data['name'] = r_user.json().get('username')
            del data['id']
            writer.writerow(data)
