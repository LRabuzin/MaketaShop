from maketashop.models import Transakcija
from maketashop.models import Maketakupljena
from maketashop.models import Napravljenaod

class TransakcijeDTO():

    def __init__(self):
        self.transakcije=Transakcije.objects.all().select_related()
        self.maketakupljena=Maketakupljena.objects.all().select_related()
        self.napravljenaod=Napravljenaod.objects.all().select_related()
    def getTransakcije(self):
        return self.price
    def getMaketakupljena(self):
        return self.maketakupljena
    def getNapravljenaOd(self):
        return self.napravljenaod
