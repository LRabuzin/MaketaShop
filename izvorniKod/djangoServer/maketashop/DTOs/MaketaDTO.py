from maketashop.models import Maketa
from maketashop.models import Materijal
from maketashop.models import Napravljenaod

class MaketaDTO():
    def __init__(self, maketaID):
        self.maketa=Maketa.objects.select_related.get(maketaid=maketaID)
        self.materijali=Materijal.objects.all().select_related()
        self.napravljenaOd=Napravljenaod.objects.filter(maketaid=maketaID)
        self.rijecnik={}
        for materijal in self.materijali:
            self.rijecnik[materijal.ime]=self.napravljenaOd.get(materijalid=materijal.materijalid)

    def getMaterijaliICijene(self):
        return self.rijecnik

    def getMaketaSlika(self):
        self.maketa.mediaid.putdodatoteke

    def getDimenzije(self):
        return self.maketa.getDimenzije()