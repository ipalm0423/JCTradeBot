from JCTradeBot.trader import Trader
from JCTradeBot.parser import DataParser
from JCTradeBot.analyzer import Analyzer
from time import sleep


"""constant"""
k_ETHUSDT = "ETHUSDT"
k_BTCUSDT = "BTCUSDT"
k_NEOUSDT = "NEOUSDT"
k_ADAUSDT = "ADAUSDT"
k_ADAETH = "ADAETH"
k_IOTABTC = "IOTABTC"

"""trader"""
trader_list = [k_ETHUSDT, k_BTCUSDT, k_NEOUSDT, k_ADAUSDT, k_ADAETH, k_IOTABTC]

def get_trader_of(symbol):
    return Trader(60, DataParser(symbol), Analyzer(symbol))


for symbol in trader_list:
    trader = get_trader_of(symbol)
    trader.start()
    sleep(1)




