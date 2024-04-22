#!/usr/bin/python3

"""
This module provides a function, `top_ten`, that queries the Reddit API to fetch and print the titles of the first 10 hot posts in a given subreddit.

The function handles invalid subreddits by printing None.

Dependencies:
- requests: The function uses the requests library to make HTTP requests to the Reddit API.
"""

from requests import get

def top_ten(subreddit):
    
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None: If the subreddit is invalid or no results are found, prints None.
    """
    if subreddit and type(subreddit) is str:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
        headers = {'user-agent': 'my-app/0.0.1'}
        params = {'limit': 10}
        req = get(url, params=params, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            data = req.json()
            posts = data.get('data', {}).get('children', {})
            for post in posts:
                print(post.get('data').get('title'))
        else:
            print(None)
