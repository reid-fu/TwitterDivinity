# had to add these lines to find src directory - evan
import sys, os, json
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from src.python.twitter_caller import TwitterCaller
from src.python.watson_nlu import WatsonNLU

twitter = TwitterCaller("../../twitter_creds")
nlu = WatsonNLU("../../watson_creds")
tweet_count = 0
max_tweet_count = 999
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
        tag_types = ["sentiment"]
        annotations = nlu.annotate(text, tag_types)

        sentString = annotations["sentiment"]["document"]["label"]

        sentInt = -2;

        if sentString == 'negative':
        	sentInt = -1
        

        elif sentString == "neutral":
        	sentInt = 0
     

        elif sentString == "positive":
        	sentInt = 1
        

        data ['tweets'].append(text)
        data ['sentiment'].append(sentInt)
    except Exception as e:
        print(e)
        continue

with open('../../results/data', 'w') as outfile:  
    json.dump(data, outfile)
