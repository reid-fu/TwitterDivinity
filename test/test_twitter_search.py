from TwitterSearch import *

try:
    #tuo = TwitterUserOrder('realDonaldTrump') # create a TwitterUserOrder
    tso = TwitterSearchOrder()
    tso.set_keywords(['Donald', 'Trump', '-filter:retweets'])
    tso.set_language('en')
    tso.set_include_entities(True)
    
    ts = TwitterSearch(
        consumer_key = 'SohKt4qmP1szCqbZql9cwkxF9',
        consumer_secret = 'uTI8sLOIuN9NJBhMrVWf11MCfKB93amj1Px3L7HjzjUs0INIpi',
        access_token = '845641999831183360-JyFj0Qw1egWynwyHBD03HSC38rgmcay',
        access_token_secret = 'KSEySafnRV8vbdSGqmebnlIs4GBLFAd5CZ32gezv7xjQJ'
    )

    for tweet in ts.search_tweets_iterable(tso):
        text = tweet['text'].encode('utf-8')
        print(text)

except TwitterSearchException as e: # catch all those ugly errors
    print(e)