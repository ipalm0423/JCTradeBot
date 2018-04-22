from binance.client import Client
from app.JCTradeBot.Model.models import OHLCVValue, AnalyzeData


class DataParser(object):
    """docstring for DataParser"""
    data_interval = 20

    def __init__(self, symbol=None):
        self.symbol = symbol
        self.client = Client("", "")
        pass

    def get_kline_in_minute(self, minutes):
        k_lines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE,
                                                    "{} minutes ago UTC".format(minutes))
        return OHLCVValue.from_data_array(k_lines)

    def get_next_data(self):
        return AnalyzeData(self.get_kline_in_minute(self.data_interval))


class TestDataParser(DataParser):
    data_index = 0

    def __init__(self, symbol=None, days_before_now=30):
        super(TestDataParser, self).__init__(symbol)
        self.days_before_now = days_before_now
        self.k_lines = self.get_kline_in_days(days_before_now)

    def get_kline_in_days(self, days=None):
        k_lines = self.client.get_historical_klines(self.symbol,
                                                    Client.KLINE_INTERVAL_1MINUTE,
                                                    "{{} days ago UTC}".format(days))
        return OHLCVValue.from_data_array(k_lines)

    def get_next_data(self):
        end_index = self.data_index + self.period

        if end_index > len(self.k_lines):
            return []

        test_data = AnalyzeData(self.k_lines[self.data_index:end_index])
        self.data_index += 1
        return test_data
