#!/usr/bin/python3
""" Contains the number_of_subscribers function """

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        res = requests.get(url)
        subreddit = res.json()
        number_of_subscribers = subreddit['data']['subscribers']
    except Exception as e:
        return 0
    return number_of_subscribers
