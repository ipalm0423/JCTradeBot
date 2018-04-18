from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer

"""constant"""
k_ETHUSDT = "ETHUSDT"
k_BTCUSDT = "BTCUSDT"

"""trader"""
eth_trader = Trader(60, DataParser(k_ETHUSDT), Analyzer(k_ETHUSDT))
btc_trader = Trader(60, DataParser(k_BTCUSDT), Analyzer(k_BTCUSDT))

eth_trader.start()
print("btc start")
btc_trader.start()

