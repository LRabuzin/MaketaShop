from maketashop.models import Transakcija
from maketashop.models import Maketakupljena
from maketashop.models import Napravljenaod
from maketashop.models import Maketa
from maketashop.models import Materijal

class TransakcijeDTO():

    def __init__(self):
        self.transakcije=Transakcija.objects.all().select_related()
        self.maketakupljena=Maketakupljena.objects.all().select_related()
        self.napravljenaod=Napravljenaod.objects.all().select_related()
        self.maketa=Maketa.objects.all().select_related()
        self.materijal=Materijal.objects.all().select_related()
        
    def getTransakcije(self):
        return self.transakcije
    def getMaketakupljena(self):
        return self.maketakupljena
    def getNapravljenaOd(self):
        return self.napravljenaod
    def getMaketa(self):
        return self.maketa
    def getMaterijal(self):
        return self.materijal
