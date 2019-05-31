from iConsultant import iconsultant
from vendor import vendor
from pwc import pwc
from ey import ey

class customer(object):
    def __init__(self):
        self.vendorName = None
        self.vendor = None
    
    def createVendor(self, vendorName):
        self.vendorName = vendorName
        self.vendor = vendor(vendorName)
    
    
    def doTask(self): 
        # This activity can be further factorized.. Not for now.
        # This version is simple Factory Method.
        # You can abstract further using Abstract Factory Method
        
        self.vendor.do_SAP_Security_audit()
        self.vendor.do_SAP_PurchaseSale_audit()
        self.vendor.do_SAP_HR_audit()