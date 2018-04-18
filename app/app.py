from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer


eth_parser = DataParser("ETHUSDT")
eth_analyzer = Analyzer("ETHUSDT")
eth_trader = Trader(5, eth_parser, eth_analyzer)


eth_trader.start()

while True:
    command = input("input your command:")

    if command == "end":
        break

    pass
