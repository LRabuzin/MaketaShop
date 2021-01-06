from maketashop.models import Maketa
from maketashop.models import Materijal
from maketashop.models import Napravljenaod

class MaketaDTO():
    def __init__(self, maketaID):
        self.maketa=Maketa.objects.select_related().get(maketaid=maketaID)
        self.materijali=Materijal.objects.all().select_related()
        self.napravljenaOd=Napravljenaod.objects.filter(maketaid=maketaID)
        self.rijecnik={}
        self.brUSkladistu={}
        for materijal in self.materijali:
            if self.napravljenaOd.filter(materijalid=materijal.materijalid).exists():
                self.rijecnik[materijal.ime]=self.napravljenaOd.get(materijalid=materijal.materijalid).cijena
                self.brUSkladistu[materijal.ime]=self.napravljenaOd.get(materijalid=materijal.materijalid).brojuskladistu
        
    def getMaterijaliICijene(self):
        return self.rijecnik
    
    def getIme(self):
        return self.maketa.ime

    def getDimenzije(self):
        return self.maketa.getDimenzije()

    def getOpis(self):
        return self.maketa.opis
    
    def getVrsta(self):
        return self.maketa.vrsta

    def getMaketaSlika(self):
        return self.maketa.mediaid.putdodatoteke
    
    def getId(self):
        return self.maketa.maketaid

    def getOsnovniMaterijal(self):
        for item in self.rijecnik.keys():
            return item
    
    def getOsnovnuCijenu(self):
        for item in self.rijecnik.values():
            return item

    def getSkladiste(self):
        return self.brUSkladistu