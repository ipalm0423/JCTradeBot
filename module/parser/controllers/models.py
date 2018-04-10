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
	def from_array(cls, array):
		return cls(array[0], array[1], array[2], array[3], array[4], array[5], array[6])
		

