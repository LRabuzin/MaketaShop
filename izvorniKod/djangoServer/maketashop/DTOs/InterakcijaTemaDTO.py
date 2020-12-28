from maketashop.models import Korisnik
from maketashop.models import Tema
from maketashop.models import Interakcija
from maketashop.models import Maketa
from maketashop.models import Prica
from maketashop.models import Multimedijaprice

class InterakcijaTemaDTO():

      def __init__(self, interakcijaID):
         interakcija = Interakcija.objects.select_related().get(interakcijaid = interakcijaID)
         self.vrsta = interakcija.vrstainterakcije
         self.naslov = interakcija.naslovinterakcije
         self.otvoren = interakcija.interakcijaotvorena
         self.korisnik = interakcija.korisnikid
         self.tema = Tema.objects.select_related().get(temaid = interakcija.temaid)
      def getVrsta(self):
         return self.vrsta
      
      def getTema(self):
         return self.tema

      def getNaslov(self):
         return self.naslov
      
      def getOtvoren(self):
         return self.otvoren



