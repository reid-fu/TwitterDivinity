from TwitterSearch import *
from src.python.twitter_caller import TwitterCaller
from src.python.watson_nlu import WatsonNLU

twitter = TwitterCaller("../twitter_creds")
nlu = WatsonNLU("../watson_creds")
    
for tweet in twitter.search(['Donald', 'Trump']):
    try:
        text = tweet['text']
        sentiment = nlu.annotate(text, ["sentiment"])
        print(text)
        print(sentiment)
    except Exception as e:
        print(e)
        continue