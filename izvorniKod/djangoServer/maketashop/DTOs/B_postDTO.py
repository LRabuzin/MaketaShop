from maketashop.models import Prica
from maketashop.models import Napravljenaod
from maketashop.models import Komentar
from maketashop.models import Korisnik

class B_postDTO():

    def __init__(self, id, lajkao):
        self.prica=Prica.objects.select_related().get(pricaid=id);
        self.napod = Napravljenaod.objects.get(maketaid=self.prica.maketaid)
        self.komentari = Komentar.objects.filter(pricaid=self.prica.pricaid)
        self.lajk = lajkao;
        self.brojLajkova = Prica.
    def getPrica(self):
        return self.prica
    def getNapod(self):
        return self.napod
    def getKomentari(self):
        return self.komentari
    def getLajk(self):
        return self.lajk;
