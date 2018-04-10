import parser
import time
import asyncio
import threading

class Trader(object):
	"""docstring for Trader"""

	_loop = None
	_thread = None
	_shouldRunning = True

	def __init__(self, period, parser, analyzer):
		super(Trader, self).__init__()
		self.period = period
		self.parser = parser
		self.analyzer = analyzer
		pass
		
	def start(self):
		self._loop = asyncio.get_event_loop()
		self._thread = threading.Thread(target=self.run_trading_loop)
		self._thread.start()
		pass

	def stop(self):
		self._shouldRunning = False
		pass

	def run_trading_loop(self):
		self._loop.run_until_complete(self.trading_async())
		self._loop.close()
		self._loop = None
		print("close loop")
		pass

	async def trading_async(self):
		print("start trading")
		while True:
			#parsing
			klines = self.parser.get_kline_30()
			print("get data from time:{} to time:{}".format(klines[0].open_time, klines[-1].close_time))

			#analytic
			if not self._shouldRunning:
				break
				pass
			#order

			#sleep
			time.sleep(self.period)


