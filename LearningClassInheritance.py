class indian:
    def __init__(self):
        self.aadhar = 123
        self.name = "Ronak"
        self.dob = "14 June 2005"

    def tax_paid(self):
        print("Nirmala tai maaf kardo")



class delhite(indian):
    def __init__(self):
        super().__init__()
        self.momos = True
        self.gaali = "bc"

    def tax_paid(self):
        super().tax_paid()
        print("atta batta albatta, kaash katt jaaye nirmala tai ka patta")
    
bablu = delhite()
bablu.tax_paid()