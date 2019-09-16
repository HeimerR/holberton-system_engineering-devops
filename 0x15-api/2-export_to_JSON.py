#!/usr/bin/python3
"""  export data in the CSV format. """
import json
import requests
from sys import argv


if __name__ == "__main__":
    """ main code """
    params = {"userId": argv[1]}
    r_info = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params=params)
    r_user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(argv[1]))
    r_info_filtered = list(
        filter(
            lambda elem: elem.get("userId") == int(
                argv[1]),
            r_info.json()))
    for dictionary in r_info_filtered:
        dictionary["task"] = dictionary.pop("title")
        del dictionary["userId"]
        del dictionary["id"]
        dictionary["username"] = r_user.json().get("username")
    data = {argv[1]: r_info_filtered}
    with open("{}.json".format(argv[1]), "w") as f:
        json.dump(data, f)
