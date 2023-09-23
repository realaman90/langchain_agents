import os
from datetime import datetime, timezone
import logging
import tweepy
from dotenv import load_dotenv

load_dotenv()


logger = logging.getLogger("twitter")


auth = tweepy.OAuthHandler(
    os.getenv("TWITTER_API_KEY"), os.getenv("TWITTER_API_SECRET")
)
auth.set_access_token(
    os.getenv("TWITTER_ACCESS_TOKEN"), os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)


def scrape_user_tweets(username, num_tweets=5):
    """Scrape a user's original tweets
    (i.e. not retweets) and return a list of dictoinaries.
    Each dictionary contains three fields: "time_posted" (relative to now), "text", and "url".
    """

    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list = []

    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dict["text"] = tweet.text
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

    return tweet_list
