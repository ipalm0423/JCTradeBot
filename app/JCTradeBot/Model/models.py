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
    def start_date_str(self):
        ohcv = self.k_lines[0]  # type: OHLCVValue
        return ohcv.open_date_str

    @property
    def end_date_str(self):
        ohcv = self.k_lines[-1]  # type: OHLCVValue
        return ohcv.close_date_str

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

    """constant"""
    k_going_up = "[ 向上 ]"
    k_going_down = "[ 向下 ]"

    """property"""
    is_change_quickly = False
    is_rise = False

    def __init__(self, symbol):
        super(AnalyzeResult, self).__init__()
        self.symbol = symbol
        pass

    def __str__(self):
        description = "\nAnalyze Result:"

        if self.is_change_quickly:
            description += "\n warning: is change quickly"

        return description

    def reminder_msg(self):
        if self.is_change_quickly:
            direction = self.k_going_up if self.is_rise else self.k_going_down
            return "{}貨幣{}大量變化中，請注意".format(self.symbol, direction)

        return None
