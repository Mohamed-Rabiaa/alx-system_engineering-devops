#!/usr/bin/python3
""" Contains the number_of_subscribers function """

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'my_app/0.0.1'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        result = res.json()
        number_of_subscribers = result.get('data').get('subscribers')
        return number_of_subscribers
    else:
        return 0
