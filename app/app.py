from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer
from time import sleep
from app.JCTradeBot.constant import *
from .messenger import JCBMessenger

"""trader"""
trader_list = [k_ETHUSDT, k_BTCUSDT, k_NEOUSDT, k_ADAUSDT, k_ADAETH, k_IOTABTC]
messenger = JCBMessenger()

def get_trader_of(symbol):
    return Trader(60, DataParser(symbol), Analyzer(symbol), messenger)


for symbol in trader_list:
    trader = get_trader_of(symbol)
    trader.start()
    sleep(1)




