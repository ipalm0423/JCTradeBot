from binance.client import Client
from .models import OHLCVValue


class DataParser(object):
    """docstring for DataParser"""

    def __init__(self, symbol):
        self.symbol = symbol
        self.client = Client("", "")
        pass

    def get_kline_in_minute(self, minutes):
        k_lines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE,
                                                    "{} minutes ago UTC".format(minutes))
        return OHLCVValue.from_data_array(k_lines)
