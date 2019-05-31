from abc import ABC, abstractmethod

class ibeverage(ABC):

    @abstractmethod
    def printCost(self):
        pass
    
    @abstractmethod
    def printDescription(self):
        pass