from app.JCTradeBot.analyzer import Analyzer
from app.JCTradeBot.constant import *
from app.JCTradeBot.parser import TestDataParser
from app.JCTradeBot.trader import TestTrader

test_days_before = 1


def get_test_trader_of(symbol):
    return TestTrader(0, TestDataParser(symbol, test_days_before), Analyzer(symbol))


test_trader = get_test_trader_of(k_ETHUSDT)
test_trader.start()
