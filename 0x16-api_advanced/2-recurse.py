#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list, optional): A list of titles to accumulate. If not provided, a new list will be created.
    after (str, optional): The 'after' parameter for pagination. If not provided, the request starts from the beginning.
    
    Returns:
    list: A list of titles of all hot articles in the given subreddit.
    None: If the subreddit is invalid or there are no results found.
    """
    
    if hot_list is None:
        hot_list = []
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'python:recurse_function:v1.0 (by /u/yourusername)'}
    params = {
        'limit': 100,
        'after': after
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])
        
        if not children:
            return None
        
        for child in children:
            hot_list.append(child['data']['title'])
        
        after = data.get('data', {}).get('after')
        
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        return None
    else:
        return None
