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
        return cls(int(array[0]), float(array[1]), float(array[2]), float(array[3]),
                   float(array[4]), float(array[5]), int(array[6]))

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
    def duration_time_in_second(self):
        return (self.close_time - self.open_time) * 1000

    @property
    def price_change(self):
        return self.close_price - self.open_price

    @property
    def price_change_percent(self):
        return self.price_change / self.open_price

    @property
    def price_change_velocity(self):
        return self.price_change / self.duration_time_in_second

    @property
    def price_change_percent_velocity(self):
        return self.price_change_percent / self.duration_time_in_second


class AnalyzeData(object):
    """docstring for AnalyzeData"""

    def __init__(self, k_lines):
        super(AnalyzeData, self).__init__()
        self.k_lines = k_lines
        pass

    @property
    def price_change_percent_sum(self):
        return self.price_change_percent_sum_from_last(len(self.k_lines))

    @property
    def volume_sum(self):
        sum_of_volume = 0

        for k_line in self.k_lines:  # type: OHLCVValue
            sum_of_volume += k_line.volume

        return sum_of_volume

    def volume_sum_from_last(self, count: 'int'):
        arr_len = len(self.k_lines)
        sum_of_volume = 0
        start_index = (arr_len - count) if arr_len >= count else 0

        for i in range(start_index, arr_len):  # type: OHLCVValue
            sum_of_volume += self.k_lines[i].volume

        return sum_of_volume

    def price_change_percent_sum_from_last(self, count: int):
        arr_len = len(self.k_lines)
        sum_of_change = 0
        start_index = (arr_len - count) if arr_len >= count else 0

        for i in range(start_index, arr_len):  # type: OHLCVValue
            sum_of_change += self.k_lines[i].price_change_percent

        return sum_of_change

    def volume_SMA(self, count: int):
        return self.volume_sum_from_last(count) / count


class AnalyzeResult(object):
    """docstring for AnalyzeResult"""
    is_rise_quickly = False

    def __init__(self):
        super(AnalyzeResult, self).__init__()
        pass
