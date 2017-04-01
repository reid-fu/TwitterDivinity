import json
from TwitterSearch import *

class TwitterCaller(object):
    def __init__(self, creds_file):
        self.creds = TwitterCreds(creds_file)
        self.twitter_search = TwitterSearch(
            self.creds.consumer_key,
            self.creds.consumer_secret,
            self.creds.access_token,
            self.creds.access_token_secret
        )
    def search(self, keyword_list):
        tso = TwitterSearchOrder()
        tso.set_keywords(keyword_list)
        tso.set_language('en')
        tso.set_include_entities(False)
        return self.twitter_search.search_tweets_iterable(tso)
    
class TwitterCreds(object):
    def __init__(self, file_path):
        with open(file_path) as creds:
            twitter_creds = json.load(creds)
            self.consumer_key = twitter_creds['consumer_key']
            self.consumer_secret = twitter_creds['consumer_secret']
            self.access_token = twitter_creds['access_token']
            self.access_token_secret = twitter_creds['access_token_secret']