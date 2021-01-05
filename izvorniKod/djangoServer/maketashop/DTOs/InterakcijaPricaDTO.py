from maketashop.models import Korisnik
from maketashop.models import Tema
from maketashop.models import Interakcija
from maketashop.models import Maketa
from maketashop.models import Prica
from maketashop.models import Multimedijaprice

class InterakcijaPricaDTO():

      def __init__(self, interakcijaID):
         interakcija = Interakcija.objects.select_related().get(interakcijaid = interakcijaID)
         self.vrsta = interakcija.vrstainterakcije
         self.naslov = interakcija.naslovinterakcije
         self.otvoren = interakcija.interakcijaotvorena
         self.korisnik = interakcija.korisnikid
         self.prica = Prica.objects.select_related().get(pricaid = interakcija.pricaid.pricaid)

         self.multimedija = Multimedijaprice.objects.select_related().filter(pricaid = interakcija.pricaid.pricaid).order_by('poredakuprici')

         self.svaMedija=[]

         for medija in self.multimedija:
            self.svaMedija.append((medija.mediaid.vrstamedije,medija.mediaid.putdodatoteke))

      def getVrsta(self):
         return self.vrsta
      
      def getPrica(self):
         return self.prica

      def getNaslov(self):
         return self.naslov
      
      def getOtvoren(self):
         return self.otvoren
      
      def getMultimedija(self):
         return self.multimedija
      
      def getSvaMedija(self):
        return self.svaMedija
      
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