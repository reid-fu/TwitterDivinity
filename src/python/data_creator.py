# had to add these lines to find src directory - evan
import sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from src.python.twitter_caller import TwitterCaller
from src.python.watson_nlu import WatsonNLU

twitter = TwitterCaller("../../twitter_creds")
nlu = WatsonNLU("../../watson_creds")
tweet_count = 0
max_tweet_count = 500
data = {}
data ['tweets'] = []
data ['sentiment'] = []

for tweet in twitter.search(['Donald', 'Trump', '-filter:retweets']):
    if tweet_count > max_tweet_count:
        break
    else:
        tweet_count += 1
        print(tweet_count)
    try:
        text = tweet['text']
        tag_types = ["sentiment", "categories", "concepts", "emotion", "entities"]
        annotations = nlu.annotate(text, tag_types)
        data['tweets'].append(text)
        data['sentiment'].append(annotations["sentiment"]["document"]["label"])
    except Exception as e:
        print(e)
        continue

with open('../results/data', 'w') as outfile:  
    json.dump(data, outfile)