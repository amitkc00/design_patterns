
from abc import ABC, abstractmethod

class iweather(ABC):
    @abstractmethod
    def subscribeElem(self):
        pass
    
    @abstractmethod
    def unsubscribeElem(self):
        pass
    
    @abstractmethod
    def notify(self):
        pass
