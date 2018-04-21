import time
import asyncio
import threading
from .models import AnalyzeData, AnalyzeResult
from .messenger import JCBMessenger
from .parser import DataParser


class Trader(object):
    """docstring for Trader"""

    _thread = None
    _shouldRunning = True

    def __init__(self, period, parser, analyzer, messenger=None):
        super(Trader, self).__init__()
        self.period = period
        self.parser = parser  # type: DataParser
        self.analyzer = analyzer
        self.messenger = messenger
        pass

    def start(self):
        self._thread = threading.Thread(target=self.run, args=())
        self._thread.daemon = True
        self._thread.start()
        pass

    def stop(self):
        self._shouldRunning = False
        pass

    def run(self):
        print("Trading Start: [ {} ]".format(self.parser.symbol))
        while True:
            # check loop
            if not self._shouldRunning:
                break
                pass

            # parsing
            k_lines = self.parser.get_kline_in_minute(20)
            new_data = AnalyzeData(k_lines)

            # analytic
            result = self.analyzer.update_new_data(new_data)  # type: AnalyzeResult

            # message
            self.messenger.send_text(result.reminder_msg())

            # sleep
            time.sleep(self.period)



class TestTrader(Trader):
    def __init__(self):