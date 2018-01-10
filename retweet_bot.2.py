import tweepy
import re
import fileinput
from credentials import *
import threading

auth = tweepy.OAuthHandler(key, secret_key)
auth.set_access_token(token, secret_token)
api = tweepy.API(auth)

def get_tweets(old_id):
  new_tweets = api.user_timeline(screen_name='realDonaldTrump', count=1, tweet_mode='extended')
  tweet_id = [tweet.id for tweet in new_tweets]
  new_id = tweet_id[0]

  if new_id > old_id:
    tweets = [[tweet.full_text] for tweet in new_tweets]
    old_id = new_id

  with open('drivel.txt', 'w') as file:
    for t in tweets:
      file.write("Deaw Diawy, %s\n" % t)

  with open('drivel.txt', 'r') as drivel, open('diary.txt', 'w') as diary:
    data = drivel.readlines()
    for t in data:
      data = t.replace('r', 'w').replace('R', 'W').replace('[', '').replace(
        ']', '').replace('l', 'w').replace('L', 'W').replace('\'', '')
      data = data[:277]
      diary.write(data)
    data = drivel.readlines()

def send_tweet():
  with open('diary.txt', 'r') as diary:
    lines = diary.readlines()
    for line in lines:
      try:
        print(line)
        api.update_status(line)
      except tweepy.TweepError as e:
        print(e.reason)


def loop_it():
  threading.Timer(60, loop_it).start()
  get_tweets(old_id)
  send_tweet()


old_id = 0
loop_it()





# with open('drivel.txt', 'w') as drivel:
#   for t in drivel:
#     drivel = [t.replace('r', 'w').replace('R', 'W').replace('[\'', '').replace(
#       ']', '').replace('l', 'w').replace('L', 'W').replace('\'', '') for t in drivel]
#   drivel.write(drivel)
#   #data = re.sub(r"http\S+", "", data)

# with open('diary.txt', 'a+') as diary:
#   data = diary.readlines()
#   for line in data:
#     line = line[:25]
#     diary.write(line)
#   #url = re.sub(r"http\S+", "", data)
#   #diary.write(url)