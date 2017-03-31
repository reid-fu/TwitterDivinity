from TwitterSearch import *
import sys

try:
    #tuo = TwitterUserOrder('realDonaldTrump') # create a TwitterUserOrder
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['Donald', 'Trump']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information
    
    ts = TwitterSearch(
        consumer_key = 'SohKt4qmP1szCqbZql9cwkxF9',
        consumer_secret = 'uTI8sLOIuN9NJBhMrVWf11MCfKB93amj1Px3L7HjzjUs0INIpi',
        access_token = '845641999831183360-JyFj0Qw1egWynwyHBD03HSC38rgmcay',
        access_token_secret = 'KSEySafnRV8vbdSGqmebnlIs4GBLFAd5CZ32gezv7xjQJ'
    )

    # start asking Twitter about the timeline
    for tweet in ts.search_tweets_iterable(tso):
        user = tweet['user']['screen_name'].encode('utf-8')
        text = tweet['text'].encode('utf-8')
        print( '@%s tweeted: %s' % ( user, text ) )

except TwitterSearchException as e: # catch all those ugly errors
    print(e)