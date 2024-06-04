#!/usr/bin/python3
""" Contains the top_ten function """

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'my_app/0.0.1'}
    params = {'limit': 10}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=params)
    if res.status_code == 200:
        posts = res.json()
        for post in posts.get('data').get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
