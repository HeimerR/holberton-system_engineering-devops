#!/usr/bin/python3
""" calls Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns number of subs given a subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v1.0 (by /u/heimer_r)"}
    subs = requests.get(url, headers=agt, allow_redirects=False)
    if subs.status_code != 200:
        return (0)
    num_subs = subs.json().get("data").get("subscribers")
    return (num_subs)
