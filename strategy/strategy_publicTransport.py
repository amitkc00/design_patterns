from strategy import istrategy

class publicTransport_map(istrategy):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def buildmaps(self):
        print("This is Public Transport map")
    