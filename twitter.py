import tweepy
import pandas as pd

def get_twitter_text(s):

    api_key = 'lEy67MdXngtKflMC38kJr1u6w'
    api_key_secret = 'FMTwcOA321V8cuMW8Hq1tkc3PhZnSBBKDKeQPlvVCF4gwfmrHG'
    access_token = '1500079761326219264-gmLQfR9XMh7fhWsRHu7W9zCplxOlpM'
    access_token_secret = 'C4La0DrHqJDsHW9QMo452JakPOHZK8KwuDDYum8V1qQSO'

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    keywords = '#'+s+'-filter:retweets'
    tweets=tweepy.Cursor(api.search_tweets,q=keywords,lang="en",tweet_mode="extended").items(1000)
    columns = ['Tweet']
    data = []
    for tweet in tweets:
        data.append([ tweet.full_text])
    df = pd.DataFrame(data, columns=columns)
    #print(df)
    return df
