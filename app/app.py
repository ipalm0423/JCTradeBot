from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer


eth_parser = DataParser("ETHUSDT")
eth_analyzer = Analyzer("ETHUSDT")
eth_trader = Trader(3, eth_parser, eth_analyzer)


eth_trader.start()

