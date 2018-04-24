from app.JCTradeBot.Analyzer.analyzer import Analyzer
from app.JCTradeBot.constant import *
from app.JCTradeBot.Parser.parser import TestDataParser
from app.JCTradeBot.Trader.trader import TestTrader
from app.JCTradeBot.Messenger.messenger import CSVMessenger


test_days_before = 1


def get_test_trader_of(symbol):
    return TestTrader(0, TestDataParser(symbol, test_days_before), Analyzer(symbol), CSVMessenger(), test_days_before)


test_trader = get_test_trader_of(k_ETHUSDT)
test_trader.start()
