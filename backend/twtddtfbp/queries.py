from twtddtfbp import cache
from twtddtfbp.models import Tweet


def cached_query(f):
    """cache function results assuming there are no arguments"""
    def wrapper(skip_cache=False):
        if not skip_cache and cache.has_key(f.__name__):
            return cache.get(f.__name__)
        print("Cache miss " + str(f.__name__))
        result = f()
        cache.set(f.__name__, result)
        return result
    return wrapper

@cached_query
def all_sorted_by_date():
    return Tweet.query.order_by(Tweet.date.desc()).all()

@cached_query
def top_by_retweets():
    return Tweet.query.order_by(Tweet.retweets.desc()).limit(10).all()

@cached_query
def top_by_likes():
    return Tweet.query.order_by(Tweet.likes.desc()).limit(10).all()
