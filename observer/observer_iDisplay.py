from abc import ABC, abstractmethod

class idisplay(ABC):
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def display(self):
        pass