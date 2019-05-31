from observer_iDisplay import idisplay

class statisticsDisplay(idisplay):

    def __init__(self, data={}):
        self.data = data
    
    def display(self):
        print("Display statistics data \n\n")
    
    def update(self,data):
        print("stats Data Updated")
        self.display()