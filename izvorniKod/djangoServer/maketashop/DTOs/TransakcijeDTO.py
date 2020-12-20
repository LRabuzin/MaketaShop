from maketashop.models import Transakcija
from maketashop.models import Maketakupljena
from maketashop.models import Napravljenaod
from maketashop.models import Maketa
from maketashop.models import Materijal
from maketashop.models import Korisnik

class TransakcijeDTO():

    def __init__(self):
        self.korisnik=Korisnik.objects.all().select_related()
        self.transakcije=Transakcija.objects.all().select_related()
        self.maketakupljena=Maketakupljena.objects.all().select_related()
        self.napravljenaod=Napravljenaod.objects.all().select_related()
        self.maketa=Maketa.objects.all().select_related()
        self.materijal=Materijal.objects.all().select_related()
        self.admin = False
        
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
    def getKorisnik(self):
        return self.korisnik
    def getAdmin(self):
        return self.admin
