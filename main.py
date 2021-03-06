from app.JCTradeBot.Trader.trader import Trader
from app.JCTradeBot.Parser.parser import DataParser
from app.JCTradeBot.Analyzer.analyzer import PumpAnalyzer
from time import sleep
from app.JCTradeBot.constant import *
from app.JCTradeBot.Messenger.messenger import JCBMessenger

"""trader"""
trader_list = [k_ETHUSDT, k_BTCUSDT, k_NEOUSDT, k_ADAUSDT, k_ADAETH, k_IOTABTC]
messenger = JCBMessenger()


def get_trader_of(symbol):
    return Trader(60, DataParser(symbol), PumpAnalyzer(symbol), messenger)


for symbol in trader_list:
    trader = get_trader_of(symbol)
    trader.start()
    sleep(1)




