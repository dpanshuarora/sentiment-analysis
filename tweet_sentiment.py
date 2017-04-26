import sys
import json
import re

class Tweets(object):
  def __init__(self, tweet_file):
    self.tweets = self.load_tweets(tweet_file)

  def load_tweets(self, tweet_file):
    tweets = []
    for line in tweet_file:
      tweets.append(json.loads(line))
    return [tweet['text'] for tweet in tweets if 'text' in tweet]


    
def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  twitter = Tweets(tweet_file)  

  scores = {} #initialize an empty directory
  for line in sent_file:
    term, score = line.split("\t") #the file is tab-delimited.
    scores[term] = int(score) # Convert the score to an integer.

  tweets = ()
  rgx = re.compile("([\w][\w']*\w)")    
  for tweet in twitter.tweets:
    score = 0 #initialize score for each tweet to 0
    for word in re.findall(rgx, tweet):
      if scores.get(word) is not None:
        score+=scores.get(word)
    tweets = (tweet, score)

  for tweet in tweets:
    print tweet, score
    print("\n")

if __name__ == '__main__':
  main()
