#!/usr/bin/python3
""" calls the Reddit API and prints the titles of the first 10 hot posts """
import requests


def top_ten(subreddit):
    """ returns the first 10 hot posts given a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v1.1 (by /u/heimer_r)"}
    payload = {"limit": "10"}
    hot = requests.get(url, headers=agt, params=payload, allow_redirects=False)
    if hot.status_code != 200:
        print("None")
    else:
        hot_list = hot.json().get("data").get("children")
        hot_titles = [post.get("data").get("title") for post in hot_list]
        print(*hot_titles, sep='\n')
