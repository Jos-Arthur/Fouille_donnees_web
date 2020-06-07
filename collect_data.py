#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 6 07:05:03 2020

@author: jose-arthur
"""

from twython import Twython
import pandas as pd
import urllib3
import yaml as ym

urllib3.disable_warnings(urllib3.exceptions.InsecurePlatformWarning)

API_KEY = 'LafZ0C6RH5Xi9wKoPUtUc2p5M'

API_SEC = 'ajsmO7BNqHbwxWq7GmxpxG0Jet4ZozpUmzEXFUs5fQuxpwUGlt'

twitter = Twython(API_KEY,API_SEC)

user_data = twitter.show_user(user_id = user)
print(user_data.text)


# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
results = twitter.cursor(twitter.search, q="#WhatIDoNow", result_type='recent', count=25, tweet_mode='extended')

max_str_id = None
for _result in results:
    str_id = _result['id_str']
    if str_id > max_str_id:
        max_str_id = str_id

    # if tweet_mode='extended', use _result['full_text']
    text = _result['text'] if 'text' in _result else _result['full_text']

    # check if is retweet
    is_retweet = True if 'retweeted_status' in _result or 'quoted_status' in _result else False

    # generate tweet url
    user_id = _result['user']['id_str']
    username = _result['user']['screen_name']
    post_id = _result['id_str']
    url = "https://twitter.com/{}/status/{}".format(username, post_id) 

    # hashtags
    hashtags = [_hashtag['text'].lower() for _hashtag in _result['entities']['hashtags']]

# you might want to save max_str_id if you plan to use since_id in next query.
results = twitter.cursor(twitter.search, q="#WhatIDoNow", result_type='recent', count=25, tweet_mode='extended', since_id=max_str_id)

for _result in results:
    fichier = open("terrorism_data.json", "a")
    fichier.write(_result)
    fichier.close()
    
with open("terrorism_data.json", "r") as fichier:
	print (fichier.read())

