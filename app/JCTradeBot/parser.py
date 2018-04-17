from binance.client import Client
from .models import OHLCVValue


class DataParser(object):
    """docstring for DataParser"""

    def __init__(self, symbol):
        self.symbol = symbol
        self.client = Client("", "")
        pass

    def get_kline_30(self):
        k_lines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
        temp = []

        for k_line in k_lines:
            new_value = OHLCVValue.from_array(k_line)
            temp.append(new_value)

        return temp

    def get_kline_in_minute(self, minutes):
        k_lines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE,
                                                    "{} minutes ago UTC".format(minutes))
        temp = []

        for k_line in k_lines:
            new_value = OHLCVValue.from_array(k_line)
            temp.append(new_value)

        return temp
