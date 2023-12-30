from ast import Dict, List
from typing import Any
from secrets import  CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from connection import trends_collection
from constants import BRAZIL_WOE_ID


def _get_trends(WOE_id: int) -> List[Dict[str, Any]]:
    auth = tweepy.OAuthHandler(consumer_key= CONSUMER_KEY, consumer_secret= CONSUMER_SECRET)

    auth.set_access_token(ACCESS_TOKEN_SECRET, ACCESS_TOKEN)

    api = tweepy.API(auth)

    trends = api.trends_place(BRAZIL_WOE_ID)

    for tweet in trends:
        print (tweet)

    print(trends)
    return trends[0]['trends']

def get_trends_from_mongo()-> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)

def save_trends() -> None:
    trends = trends_collection.find({})
    
    if not list(trends):
        trends = _get_trends(WOE_id=BRAZIL_WOE_ID)
        trends_collection.insert_many(trends)
