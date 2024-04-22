#!/usr/bin/python3

"""
This module provides a function, `top_ten`, that queries the Reddit API to fetch and print the titles of the first 10 hot posts in a given subreddit.

The function handles invalid subreddits by printing None.

Dependencies:
- requests: The function uses the requests library to make HTTP requests to the Reddit API.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None: If the subreddit is invalid or no results are found, prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python:top_ten_function:v1.0 (by /u/yourusername)'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        if not children:
            print(None)
            return

        for child in children[:10]:
            print(child['data']['title'])

    elif response.status_code == 404:
        print(None)
    else:
        print(None)
