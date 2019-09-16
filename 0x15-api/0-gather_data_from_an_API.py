#!/usr/bin/python3
"""getting info from an api"""
import requests as r
from sys import argv

if __name__ == "__main__":
    """exectute req"""
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos = r.get(todo_url)
    users = r.get(users_url)
    done, total, tasks = 0, 0, []
    for x in todos.json():
        if x.get("userId") == int(argv[1]):
            total += 1
            if x.get("completed") is True:
                done += 1
                tasks.append(x.get("title"))
    for y in users.json():
        if y.get("id") == int(argv[1]):
            user = y.get("name")

    print("Employee {} is done with tasks({}/{}):"
          .format(user, done, total))

    for task in tasks:
        print("\t {}".format(task))
