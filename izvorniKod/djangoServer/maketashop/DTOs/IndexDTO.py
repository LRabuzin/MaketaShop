from maketashop.models import Prica
from maketashop.models import Multimedijaprice

class jednaPrica():
    def __init__(self, pricaID):
        self.prica=Prica.objects.select_related().get(pricaid=pricaID)
        medijaprice=Multimedijaprice.objects.select_related().filter(pricaid=prica.pricaid)
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
                    self.slika=medijaprice
                
            if medija.mediaid.vrstamedije=='tekst':
                if mintekst==None:
                    mintekst=medija.poredakuprici
                if minslika>=medija.poredakuprici:
                    minslika=midija.poredakuprici
                    self.tekst=medijaprice

    def getNaslov(self):
        return self.prica.naslovprice

    def getSlika(self):
        return self.slika
    
    def getTekst(self):
        return self.tekst

class IndexDTO():
    def __init__(self):
        self.price=Prica.objects.all().select_related().filter(objavljena=True)
        self.svePrice=[]
        for prica in self.price:
            if prica.objavljena:
                self.svePrice.append(jednaPrica(prica.pricaid))
            
    def getPrice(self):
        return self.svePrice