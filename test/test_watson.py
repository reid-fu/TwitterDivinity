# had to add these lines to find src directory - evan
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from TwitterSearch import *
from src.python.twitter_caller import TwitterCaller
from src.python.watson_nlu import WatsonNLU

twitter = TwitterCaller("../twitter_creds")
nlu = WatsonNLU("../watson_creds")
tweet_count = 0
max_tweet_count = 20

for tweet in twitter.search(['Donald', 'Trump']):
    if tweet_count > max_tweet_count:
        break
    else:
        tweet_count += 1
    try:
        text = tweet['text']
        tag_types = ["sentiment", "categories", "concepts", "emotion", "entities"]
        annotations = nlu.annotate(text, tag_types)
        print(text)
        print(annotations["sentiment"])
        print(annotations["categories"])
        print(annotations["concepts"])
        print(annotations["emotion"])
        print(annotations["entities"])
        print("")
    except Exception as e:
        print(e)
        continue