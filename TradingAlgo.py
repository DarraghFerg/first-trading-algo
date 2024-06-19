import yfinance as yf
import pandas as pd


from apscheduler.schedulers.blocking import BlockingScheduler
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
from oandapyV20.contrib.requests import *
from oanda_candles import Pair, Gran, CandleClient

'''from config import access_token, accountID''' #will write config file for api keys

''''''''''''''''''''''''''

dataF = yf.download("EURUSD=X", start="2024-6-5", end="2024-6-7", interval='1h')
dataF.iloc[:,:]


def get_candles(n):
    access_token='#####'
    client = CandleClient(access_token, real=False)
    collector = client.get_collector(Pair.EUR_USD, Gran.M15)
    candles = collector.grab(n)
    return candles

candles = get_candles(3)
for candle in candles:
    print(float(str(candle.bid.o)))




