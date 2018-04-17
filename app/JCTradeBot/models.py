import datetime


class OHLCVValue:
    def __init__(self, open_time, open_price, highest_price, lowest_price, close_price, volume, close_time):
        self.open_time = open_time
        self.open_price = open_price
        self.highest_price = highest_price
        self.lowest_price = lowest_price
        self.close_price = close_price
        self.volume = volume
        self.close_time = close_time

    @classmethod
    def from_datas(cls, array):
        return cls(array[0], array[1], array[2], array[3], array[4], array[5], array[6])

    @classmethod
    def from_data_array(cls, k_lines):
        temp = []

        for k_line in k_lines:
            new_value = OHLCVValue.from_datas(k_line)
            temp.append(new_value)
            pass

        return temp

    @property
    def open_date_str(self):
        return datetime.datetime.fromtimestamp(self.open_time / 1000).strftime('%Y-%m-%d %H:%M:%S')
        pass

    @property
    def close_date_str(self):
        return datetime.datetime.fromtimestamp(self.close_time / 1000).strftime('%Y-%m-%d %H:%M:%S')

    @property
    def mid_time(self):
        return (self.open_time + self.close_time) / 2

    @property
    def duration_time(self):
        return self.close_time - self.open_time

    @property
    def price_change(self):
        return self.close_price - self.open_price

    @property
    def price_change_percent(self):
        return self.price_change / self.open_price

    @property
    def price_change_velocity(self):
        return self.price_change / self.duration_time

    @property
    def price_change_percent_velocity(self):
        return self.price_change_percent / self.duration_time


class AnalyzeData(object):
    """docstring for AnalyzeData"""

    def __init__(self, k_lines):
        super(AnalyzeData, self).__init__()
        self.k_lines = k_lines
        pass


class AnalyzeResult(object):
    """docstring for AnalyzeResult"""

    def __init__(self, slope):
        super(AnalyzeResult, self).__init__()
        self.slope = slope
        pass
