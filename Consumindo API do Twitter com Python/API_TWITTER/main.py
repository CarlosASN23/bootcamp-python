from ast import List

from pydantic import BaseModel
from tweepy import tweepy
from fastapi import FastAPI
from service import get_trends, get_trends_from_mongo, save_trends
import uvicorn
from constants import BRAZIL_WOE_ID




class TrendItem(BaseModel):
    name: str
    url: str

BRAZIL_WOE_ID = 23424768

app = FastAPI()

@app.get('/trends/', response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mongo

if __name__ == '__main__':
    trends = get_trends_from_mongo()

    if not list(trends):
       save_trends()

    uvicorn.run(app, host='0.0.0.0', port=8000)