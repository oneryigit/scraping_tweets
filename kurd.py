#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 18:18:08 2022

@author: oneryigit
"""
import os
os.getcwd()
os.chdir('/Users/oneryigit/Desktop/scrape')

import snscrape.modules.twitter as sntwitter
import pandas as pd

keyword=("(Mevsimlik%20işçi%20kürt) OR (kürt%20işçi) OR (kürt%20ırkçı%20saldırı) OR (kürt%20tarım%20saldırı) OR (kürt%20tarım%20işçi%20saldırı) OR (kürt%20inşaat%20saldırı) OR (doğulular%20saldırı) OR (geçmiş%20husumet%20kürt) OR (insan%20haklari%20ihlal%20kürt) OR (galeyana%20geldi%20kürt) OR (karşıt%20grup%20çatışma%20kürt)")

tweets=[]
limit =100000000

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + '  since:2006-01-01 until:2022-11-26 lang:tr ').get_items()):
    if len(tweets)==limit:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.user.username, tweet.content, tweet.user.location, tweet.url])
        
df=pd.DataFrame(tweets, columns=['Date','ID', 'username', 'Content', 'Location', 'URL'])

df.to_csv('tweets2006-2022.csv')
