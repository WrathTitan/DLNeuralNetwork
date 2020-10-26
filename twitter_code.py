from tweepy import OAuthHandler
from tweepy import API
import tweepy
import pandas as pd

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth,wait_on_rate_limit=True)
class scraptweets:
  def user_tweets(search_word,date_since,date_until):
    try:
      tweets = tweepy.Cursor(api.search,q=search_word+"-filter:retweets",lang="en",since=date_since,until=date_until).items(100)
      users_locs = []
      analysis = []
      for tweet in tweets:
        users_locs.append([tweet.text])
      tweet_text = pd.DataFrame(data=users_locs,columns=["Tweets"])
      tweet_text.to_csv('/content/drive/My Drive/data preprocessing/'+ search_word +'.csv')
      searchwords = []
      tweet_text['Tweets'] = tweet_text['Tweets'].str.lower()
      for x in range(len(searchwords)):
        analysis.append(tweet_text[tweet_text['Tweets'].str.contains(searchwords[x])])
      tweet_text = pd.DataFrame(data=analysis)
      tweet_text.to_csv('/content/drive/My Drive/data preprocessing/'+ search_word +' analysis'+'.csv')
    except BaseException as e:
      tweet_text = pd.DataFrame(data=e,columns=["errors"])
      tweet_text.to_csv('/content/drive/My Drive/data preprocessing/'+ search_word +'.csv')          
scraptweets.user_tweets('narendra modi','2020-7-10','2020-7-15')