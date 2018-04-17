class Analyzer(object):
    maxBudget = 0
    currentPurchase = 0

    """docstring for Analyzer"""

    def __init__(self, symbol):
        super(Analyzer, self).__init__()
        self.symbol = symbol
        self.update_base_data()
        self.current_data = None
        pass

    def update_base_data(self):
        pass

    def update_new_data(self, analyze_data):
        self.current_data = analyze_data

        # calculate
        # volume
        # slope

        # result
        pass
