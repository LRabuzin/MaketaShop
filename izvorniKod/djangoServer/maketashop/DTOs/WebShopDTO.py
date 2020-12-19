from maketashop.models import Maketa
from maketashop.models import Napravljenaod

class WebShopDTO():
    def __init__(self):
        self.makete=Maketa.objects.all().select_related()
        self.rijecnikMaketaMaterijaliCijene={}
        for maketa in self.makete:
            napravljenaOd=Napravljenaod.objects.filter(maketaid=maketa.maketaid)
            self.rijecnikMaketaMaterijaliCijene[maketa]=napravljenaOd
    def getMakete(self):
        return self.rijecnikMaketaMaterijaliCijene