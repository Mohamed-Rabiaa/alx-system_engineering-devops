#!/usr/bin/python3
""" Contains the number_of_subscribers function """

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user_agent': 'my_app'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        subreddit = res.json()
        number_of_subscribers = subreddit.get('data').get('subscribers')
        return number_of_subscribers
    else:
        return 0
    
