#!/usr/bin/python3
""" parses the title of all hot articles, and prints a sorted count
    of given keywords
"""
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """ returns a list of all hot posts given a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v1.1 (by /u/heimer_r)"}
    payload = {"limit": "100", "after": after}
    hot = requests.get(url, headers=agt, params=payload, allow_redirects=False)
    if hot.status_code != 200:
        return None
    else:
        posts = hot.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = hot.json().get("data").get("after")
        if after is not None:
                recurse(subreddit, hot_list, after)
        return hot_list


def count_words(subreddit, word_list):
    """ prints number of word coincedence (titles) on a subreddit """
    hot_list = recurse(subreddit)
    if hot_list is None:
        print()
    else:
        hot_str = " ".join(hot_list)
        hot_words = hot_str.split(" ")
        rst = {}
        for word in word_list:
            num = len(list(filter(lambda hot_w: hot_w == word, hot_words)))
            if num != 0:
                rst[word] = num
        if len(rst) == 0:
            print()
        else:
            for k, v in sorted(rst.items(), key=lambda x: x[1], reverse=True):
                print(k + ": " + str(v))
