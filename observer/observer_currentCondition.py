from observer_iDisplay import idisplay

class currentCondition(idisplay):

    def __init__(self, data={}):
        self.data = data
    
    def display(self):
        print("Display Current Condition \n\n")

    def update(self,data):
        print("Current Data Updated")
        self.display()