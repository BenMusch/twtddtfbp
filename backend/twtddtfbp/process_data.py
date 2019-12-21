import difflib
from itertools import islice
import time

from twtddtfbp.app import db
from twtddtfbp.models import Tweet
from twtddtfbp.twitter import get_tweets_until_id, get_tweets_by_ids


EXPECTED_TWEET = 'Today was the day Donald trump finally became president'
TOLERANCE = 10
SLEEP = 5


def process_tweets_by_ids(ids):
    chunked_ids = lists_for_twitter_api(ids)
    for chunk in chunked_ids:
        tweet_objs = get_tweets_by_ids(list(chunk))
        for tweet_obj in tweet_objs:
            process_single_tweet(tweet_obj)
        time.sleep(SLEEP)

def should_process_tweet(tweet_obj):
    diff = difflib.ndiff(EXPECTED_TWEET.lower(), tweet_obj.text.lower())
    changes =  [li for li in diff if li[0] != ' ']
    return len(changes) <= TOLERANCE

def process_single_tweet(tweet_obj):
    if not should_process_tweet(tweet_obj):
        print("Skipping tweet %s with text '%s'" % (tweet_obj.id, tweet_obj.text))
        return

    tweet_id, date, retweets, likes = tweet_obj.id, tweet_obj.created_at, \
            tweet_obj.retweet_count, tweet_obj.favorite_count

    tweet = Tweet.query.filter_by(tweet_id=str(tweet_id)).first()
    if tweet:
        tweet.retweets = retweets
        tweet.likes = likes
    else:
        tweet = Tweet(
            tweet_id=str(tweet_id),
            date=date,
            retweets=retweets,
            likes=likes
        )
    db.session.add(tweet)
    db.session.commit()

def lists_for_twitter_api(l):
    it = iter(l)
    return iter(lambda: tuple(islice(it, 99)), ())
