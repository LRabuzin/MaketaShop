from maketashop.models import Prica
from maketashop.models import Napravljenaod
from maketashop.models import Komentar
from maketashop.models import Korisnik
from maketashop.models import Multimedijaprice

class B_postDTO():

    def __init__(self, id, lajkao):
        self.prica=Prica.objects.select_related().get(pricaid=id);
        self.napod = Napravljenaod.objects.get(maketaid=self.prica.maketaid)
        self.komentari = Komentar.objects.filter(pricaid=self.prica.pricaid)
        self.lajk = lajkao;
        self.brojLajkova = Prica.getBrojLajkova;
        self.brojDislajkova = Prica.getBrojDislajkova;

        #self.prica=Prica.objects.select_related().get(pricaid=pricaID)
        medijaprice=Multimedijaprice.objects.select_related().filter(pricaid=self.prica.pricaid)
        self.slika=None
        self.tekst=None

        for medija in medijaprice:
            minslika=None
            mintekst=None
            if medija.mediaid.vrstamedije=='slika':
                if minslika==None:
                    minslika=medija.poredakuprici
                if minslika>=medija.poredakuprici:
                    minslika=medija.poredakuprici
                    self.slika=medija.mediaid.putdodatoteke
                
            if medija.mediaid.vrstamedije=='tekst':
                if mintekst==None:
                    mintekst=medija.poredakuprici
                if mintekst>=medija.poredakuprici:
                    mintekst=medija.poredakuprici
                    self.tekst=medija.mediaid.putdodatoteke
        
    def getSlika(self):
        return self.slika
    
    def getTekst(self):
        return self.tekst

    def getPrica(self):
        return self.prica
    def getNapod(self):
        return self.napod
    def getKomentari(self):
        return self.komentari
    def getLajk(self):
        return self.lajk;

    def getNaslov(self):
        return self.prica.naslovprice
    def getAutorKorisnickoIme(self):
        return self.prica.autorid.korisnickoime
    def getAutorId(self):
        return self.prica.autorid.korisnikid
    def getPredlozioKorisnickoIme(self):
        return self.prica.predloziotemuid.korisnickoime
    def getPredlozioId(self):
        return self.prica.predloziotemuid.korisnikid
    def getDatumPrice(self):
        return self.prica.datumprice
    def getCijena(self):
        return self.napod.cijena
    def getBrojLajkova(self):
        return self.prica.brojlajkova
    def getBrojDislajkova(self):
        return self.prica.brojdislajkova
