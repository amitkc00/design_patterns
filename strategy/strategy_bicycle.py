from strategy import istrategy

class bicycle_map(istrategy):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def buildmaps(self):
        print("This is bicycle map")
    