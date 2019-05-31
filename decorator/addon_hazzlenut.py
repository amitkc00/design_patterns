from ibeverage import ibeverage

class hazzlenut(ibeverage):
    def __init__(self, bevObj):
        self.beverage = bevObj
        self.cost = bevObj.cost + 0.5
        self.description = bevObj.description + ' ' + 'hazzlenut'

    def printCost(self):
        print('Hazzlenut cost = {0}'.format(self.cost))
    
    def printDescription(self):
        print('Hazzlenut description = {0}'.format(self.description))
