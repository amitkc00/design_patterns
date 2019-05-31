from observer_iDisplay import idisplay

class forecastDisplay(idisplay):

    def __init__(self, data= {}):
        self.data = data
    
    def display(self):
        print("Display forecast data \n\n")

    def update(self, data):
        print("forecast data updated")
        self.display()