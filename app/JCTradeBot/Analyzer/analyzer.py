from app.JCTradeBot.Model.models import AnalyzeData, AnalyzeResult


class Analyzer(object):
    maxBudget = 0
    currentPurchase = 0

    """index property"""
    vol_change_ratio_gate = 2
    price_change_gate = 5

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
        result = AnalyzeResult(self.symbol, analyze_data)
        print("\nanalyze {} from time:{} to time:{}".format(self.symbol,
                                                          analyze_data.start_date_str,
                                                          analyze_data.end_date_str))

        # calculate
        result.is_change_quickly = self.is_change_quickly
        result.is_rise = self.going_direction

        # judge

        return result

    @property
    def is_change_quickly(self):
        vol_change_ratio = self.current_data.volume_SMA(3) / self.current_data.volume_SMA(10)
        price_change_ratio = abs(self.current_data.price_change_percent_sum_from_last(3)
                                 / self.current_data.price_change_percent_sum_from_last(10))

        return vol_change_ratio > self.vol_change_ratio_gate and price_change_ratio > self.price_change_gate

    @property
    def going_direction(self):
        return self.current_data.price_change_percent_sum_from_last(3) > 0
