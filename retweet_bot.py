import tweepy
import sys
import time
import json
import csv
from credentials import *

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(token, secret_token)
api = tweepy.API(auth)

start_time = time.time()  # grabs the system time
keyword_list = ['python']  # track list


class listener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit

    def on_data(self, data):
        all_data = json.loads(data)
        with open('raw_tweets.json', 'w') as saveFile:
          json.dump(all_data, saveFile)
        self.fix_tweets()

        exit()

    def on_error(self, status):
        print(statuses)

    def fix_tweets(self):
      with open('raw_tweets.json', 'r') as raw_tweets, open('tweets.csv', 'a') as x_tweets:
        data = json.load(raw_tweets)
        if 'extended_tweet' in data:
          text = data['extended_tweet']['full_text']
        else:
          text = data['text']
        tweet_id = data['id_str']
        x = tweet_id + ',' + text + '\n'
        x_tweets.write(x)
      with open('tweets.csv', 'r', newline='\n') as csvfile, open('diary.csv', 'w', newline='\n') as diary:
        #data = csv.reader(csvfile, delimiter=' ')
        #write = csv.writer(diary, delimiter=' ')
        data = csvfile.readlines()
        data = [line.replace('r', 'w').replace('R', 'W').replace('l', 'w').replace('L', 'W') for line in data]
        diary.write(str(data) + '\n')





# initialize Stream object with a time out limit
twitterStream = tweepy.Stream(auth, listener(start_time, time_limit=60))
# call the filter method to run the Stream Object
twitterStream.filter(track=keyword_list, languages=['en'])
