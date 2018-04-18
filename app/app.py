from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer


eth_parser = DataParser("ETHUSDT")
eth_analyzer = Analyzer("ETHUSDT")
eth_trader = Trader(5, eth_parser, eth_analyzer)


eth_trader.start()

while True:
    command = input("\ninput your command:\n")

    if command == "end":
        break

    pass
