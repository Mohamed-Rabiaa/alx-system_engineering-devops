#!/usr/bin/python3
""" Contains the count_words function """

from collections import Counter
import re
import requests


def count_words(subreddit, word_list, after=None, counter=None):
    """
    queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces
    """
    if counter is None:
        counter = Counter()

    headers = {'User-Agent': 'python:count_words:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers=headers,
        params=params,
        allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title']
        words = re.findall(r'\b\w+\b', title.lower())
        for word in word_list:
            counter[word.lower()] += words.count(word.lower())

    if data['data']['after']:
        count_words(
            subreddit,
            word_list,
            after=data['data']['after'],
            counter=counter)
    else:
        sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counter:
            if count > 0:
                print(f'{word}: {count}')
