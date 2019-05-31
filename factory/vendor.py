from iConsultant import iconsultant
from pwc import pwc
from ey import ey

class vendor(iconsultant):

    # How can I avoid this switch cases? 
    def __init__(self, type):
        if type == 'EY':
            self.vendor = ey()
        elif type == 'PWC':
            self.vendor = pwc()

    def do_SAP_Security_audit(self):
        self.vendor.do_SAP_Security_audit()

    def do_SAP_HR_audit(self):
        self.vendor.do_SAP_HR_audit()
    
    def do_SAP_PurchaseSale_audit(self):
        self.vendor.do_SAP_PurchaseSale_audit()