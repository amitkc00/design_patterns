from abc import ABC, abstractmethod, abstractproperty, ABCMeta

class istrategy(ABC): 
    @abstractmethod
    def buildmaps(self, start, end):
        pass