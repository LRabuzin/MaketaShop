from maketashop.models import Maketa
from maketashop.models import Materijal
from maketashop.models import Napravljenaod

class MaketaDTO():
    def __init__(self, maketaID):
        self.maketa=Maketa.objects.select_related().get(maketaid=maketaID)
        self.materijali=Materijal.objects.all().select_related()
        self.napravljenaOd=Napravljenaod.objects.filter(maketaid=maketaID)
        self.rijecnik={}
        for materijal in self.materijali:
            self.rijecnik[materijal.ime]=self.napravljenaOd.get(materijalid=materijal.materijalid)

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