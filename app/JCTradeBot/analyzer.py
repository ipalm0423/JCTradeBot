class Analyzer(object):

	maxBudget = 0
	currentPurchase = 0

	"""docstring for Analyzer"""
	def __init__(self, symbol):
		super(Analyzer, self).__init__()
		self.symbol = symbol
		self.updateBaseData()
		pass

	def updateBaseData(self):
		#api/v1/ticker/24hr
		#1 year volume

		pass

	def updateNewData(self, analyzeData):
		self.currentData = analyzeData

		#calculate
		#volume
		#slope

		#result
		pass
		

		