from ibeverage import ibeverage

class vanilla(ibeverage):
    def __init__(self, bevObj):
        self.beverage = bevObj
        self.cost = bevObj.cost + 0.25
        self.description = bevObj.description + ' ' + 'vanilla'

    def printCost(self):
        print('Vanilla cost = {0}'.format(self.cost))
    
    def printDescription(self):
        print('Vanilla description = {0}'.format(self.description))
