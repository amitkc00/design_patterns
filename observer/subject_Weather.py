from subject_iWeather import iweather

class weather(iweather):

    def __init__(self):
        self.subscriberList = []
        self.data = {}

    def subscribeElem(self, dispObj):
        self.subscriberList.append(dispObj)
    
    def unsubscribeElem(self, dispObj):
        print("Item Unsubscribed")
    
    def notify(self):
        for subscribers in self.subscriberList:
            subscribers.update(self.data)