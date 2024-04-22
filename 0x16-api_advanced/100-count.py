#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""


from requests import get


def count_words(subreddit, word_list, after='', word_dict={}):
    """ A function that queries the Reddit API parses the title of
    all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not).
    If no posts match or the subreddit is invalid, it prints nothing.
    """
    if not count:
        key_words = {word.lower(): 0 for word in word_list}
        word_list = [word.lower() for word in word_list]
        count = {word.lower(): word_list.count(word.lower())
                 for word in word_list}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after, 'limit': 100}
    headers = {'user-agent': 'my-app/0.0.1'}

    req = get(url, params=params, headers=headers, allow_redirects=False)
    #  get data if request was successful
    if req.status_code == 200:
        data = req.json().get('data')
        after = data.get('after')
        posts = data.get('children')

        #  get count of key words in each title
        for post in posts:
            title = post.get('data').get('title').lower()
            words = title.split()
            for word in key_words.keys():
                key_words[word] += words.count(word)

        #  call recursive function if there's more data
        if after:
            return count_words(subreddit, word_list, key_words, count, after)
        else:
            for key in key_words.keys():
                key_words[key] *= count[key]
            key_words = sorted(key_words.items(),
                               key=lambda item: (-item[1], item[0]))
            for item in key_words:
                if item[1] > 0:
                    print("{}: {}".format(item[0], item[1]))