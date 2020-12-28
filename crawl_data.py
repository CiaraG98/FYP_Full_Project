import tweepy
from pandas import DataFrame
import time
# Credentials
consumer_key = 'riiUgzG0nHSkUGt5c521LgcnD'
consumer_key_secret = 'XkNvxIyc83Y2t1TS3TzELFmDR9ek5pHrpPUpU3W1K9oGuGBNGP'
access_token = '710798343623073792-tNUupkHcBd4WhfqaeKfDA9vhW19lAEC'
access_token_secret = '2mgo5ZEyVOTCGnYqbRzWYRSHBfmCIfZ8rvt5MNFbwrY6O'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAABNDKgEAAAAAx7i7gCsEItSD4glnaw%2BCfuFh0Ok%3DIDQvFJ02SZ5G64z1Lzd4PwhROA8pHBij7MnWCPDK3kBGW82oaJ'

# For Request
tweetsPerQuery = 100
maxTweets = 1000
hashtag = ''
userId = 'ArianaGrande'
users = ['realDonaldTrump', 'Cristiano', 'DavidDobrik',
         'KimKardashian', 'rihanna', 'ArianaGrande']

#  Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Crawling Data
print("working on", userId)
all_tweets = []
tweets = api.user_timeline(screen_name=userId, cound=200, include_rts=False, tweet_mode="extended")
"""
    for info in tweets[:3]:
        print("ID {}".format(info.id))
        print(info.created_at)
        print(info.full_text)
        print("\n")
    """
all_tweets.extend(tweets)
old_id = tweets[-1].id
while True:
    try:
        tweets = api.user_timeline(screen_name=userId, cound=200, include_rts=False, max_id=old_id-1, tweet_mode="extended")
        if len(tweets) == 0:
            break
        old_id = tweets[-1].id
        all_tweets.extend(tweets)
        if len(all_tweets) >= 3000:
            break
        print("N of tweets download till now {}".format(len(all_tweets)))

    except tweepy.TweepError:
        print("TweepError wait...")
        time.sleep(120)

# Write to csv file
outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8").decode("utf-8")] for idx, tweet in enumerate(all_tweets)]
df = DataFrame(outtweets, columns=["id", "created_at", "text"])
df.to_csv("celeb_data/%s_tweets.csv" % userId, index=False)
# df.to_csv("test_tweets.csv", index=False, encoding='utf-8')
df.head(3)
