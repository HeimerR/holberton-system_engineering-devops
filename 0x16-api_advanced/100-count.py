#!/usr/bin/python3
""" simple comment """
from operator import itemgetter
import requests


def count_words(subreddit, word_list, hot_list=[], init=0, after="null"):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    agt = {"User-Agent": "linux:1:v2.1 (by /u/heimer_r)"}
    payload = {"limit": "100", "after": after}
    hot = requests.get(url, headers=agt, params=payload, allow_redirects=False)
    if hot.status_code == 200:
        posts = hot.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = hot.json().get("data").get("after")
        if after is not None:
            count_words(subreddit, word_list, hot_list, 1, after)
        if init == 0:
            hot_str = " ".join(hot_list)
            with open('./test', 'w+') as f:
                f.write(hot_str)
                f.close()
            hot_words = hot_str.split(" ")
            word_list = list(set(word_list))
            rst = []
            for word in word_list:
                num = len(
                    list(
                        filter(
                            lambda hot_w: hot_w.lower() == word.lower(),
                            hot_words)))
                if num != 0:
                    rst.append([word, num])
            if len(rst) != 0:
                rst_sorted = sorted(rst, key=itemgetter(1, 0), reverse=True)
                for i in rst_sorted:
                    print(*i, sep=": ")
