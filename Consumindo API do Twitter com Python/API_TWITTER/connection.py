from pymongo import MongoClient

client = MongoClient("mongodb+srv://carlosalbertosn10:%3CoEnVdeFoXBrfgfJ7%3E@"
                     "cluster0.9gdl1eo.mongodb.net/")

db = client.tweeter_api
tweets_collection = db.tweets
tweets_collection.insert_one({'author':'teste','text':'texto qualquer'})