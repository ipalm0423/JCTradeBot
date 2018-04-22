import time
import threading
from .models import AnalyzeData, AnalyzeResult
from .messenger import JCBMessenger
from .parser import DataParser


class Trader(object):
    """docstring for Trader"""

    _thread = None
    _shouldRunning = True

    def __init__(self, period=None, parser=None, analyzer=None, messenger=None):
        super(Trader, self).__init__()
        self.period = period
        self.parser = parser  # type: DataParser
        self.analyzer = analyzer
        self.messenger = messenger  # type: JCBMessenger
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

            self.calculate()

            # sleep
            time.sleep(self.period)

    def calculate(self):
        # parsing
        new_data: AnalyzeData = self.parser.get_next_data()

        # analytic
        result = self.analyzer.update_new_data(new_data)  # type: AnalyzeResult

        # message
        self.messenger.send_text(result.reminder_msg())


class TestTrader(Trader):
    def __init__(self):