#from strategy import istrategy

class context(object):
    def __init__(self):
        pass
    
    def executeStrategy(self):
        self.strategy.buildmaps()
    
    def setStrategy(self, new_strategy):
        self.strategy = new_strategy