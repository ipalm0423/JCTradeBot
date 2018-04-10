from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer
import time

eth_parser = DataParser("ETHUSDT")
eth_analyzer = Analyzer()
eth_trader = Trader(3, eth_parser, eth_analyzer)


eth_trader.start()
time.sleep(10)
eth_trader.stop()