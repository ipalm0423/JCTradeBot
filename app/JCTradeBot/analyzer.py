from .models import AnalyzeData
from .models import AnalyzeResult


class Analyzer(object):
    maxBudget = 0
    currentPurchase = 0

    """index property"""
    vol_change_ratio_gate = 2
    price_change_gate = 1

    """docstring for Analyzer"""

    def __init__(self, symbol):
        super(Analyzer, self).__init__()
        self.symbol = symbol
        self.update_base_data()
        self.current_data = None
        pass

    def update_base_data(self):
        pass

    def update_new_data(self, analyze_data: AnalyzeData) -> AnalyzeResult:
        self.current_data = analyze_data
        new_result = AnalyzeResult()

        # calculate
        vol_change_ratio = self.current_data.volume_SMA(3) / self.current_data.volume_SMA(10)
        price_change_ratio = abs(self.current_data.price_change_percent_sum_from_last(3)
                                 / self.current_data.price_change_percent_sum_from_last(10))

        if vol_change_ratio > self.vol_change_ratio_gate and \
                price_change_ratio > self.price_change_gate and \
                self.current_data.price_change_percent_sum_from_last(3) > 0:
            new_result.is_rise_quickly = True
            pass

        # judge

        # result
        return new_result
