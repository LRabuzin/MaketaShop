from maketashop.models import Prica
from maketashop.models import Multimedijaprice

class jednaPrica():
    def __init__(self, pricaID):
        self.prica=Prica.objects.select_related().get(pricaid=pricaID)
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

    def getNaslov(self):
        return self.prica.naslovprice

    def getSlika(self):
        return self.slika
    
    def getTekst(self):
        return self.tekst

    def getPricaId(self):
        return self.prica.pricaid

class IndexDTO():
    def __init__(self):
        self.price=Prica.objects.all().select_related().filter(objavljena=True).order_by('-datumprice')
        self.svePrice=[]
        for prica in self.price:
            if prica.objavljena:
                self.svePrice.append(jednaPrica(prica.pricaid))
            
    def getPrice(self):
        return self.svePrice