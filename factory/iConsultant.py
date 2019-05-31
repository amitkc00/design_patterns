from abc import ABC, abstractmethod

class iconsultant (ABC):

    @abstractmethod
    def do_SAP_Security_audit(self):
        pass
    
    @abstractmethod
    def do_SAP_HR_audit(self):
        pass
    

    @abstractmethod
    def do_SAP_PurchaseSale_audit(self):
        pass