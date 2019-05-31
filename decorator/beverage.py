from ibeverage import ibeverage

class beverage(ibeverage):
    
    def __init__(self):
        self.cost = 1
        self.description = 'Beverage'
    
    def printCost(self):
        print("This is reguarl")
        print('cost = {0}'.format(self.cost))
    
    def printDescription(self):
        print('description = {0}'.format(self.description))
