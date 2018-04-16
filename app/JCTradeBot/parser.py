from binance.client import Client
from .models import OHLCVValue

class DataParser(object):
	"""docstring for DataParser"""
	def __init__(self, symbol):
		self.symbol = symbol
		self.client = Client("", "")
		pass
		
	def get_kline_30(self):
		klines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
		temp = []

		for kline in klines:
			newValue = OHLCVValue.from_array(kline)
			temp.append(newValue)
			
		return temp

	def get_kline_in_minute(self, minutes):
		klines = self.client.get_historical_klines(self.symbol, Client.KLINE_INTERVAL_1MINUTE, "{} minutes ago UTC".format(minutes))
		temp = []

		for kline in klines:
			newValue = OHLCVValue.from_array(kline)
			temp.append(newValue)
			
		return temp

