#!/usr/bin/python3
""" Contains the recurse function """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'my_app/0.0.1'}
    params = {'after': after}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=params)
    if res.status_code == 200:
        posts = res.json()
        posts_list = posts.get('data').get('children')
        after = posts.get('data').get('after')
        if not posts_list:
            return hot_list
        hot_list.extend([post.get('data').get('title') for post in posts_list])

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None
