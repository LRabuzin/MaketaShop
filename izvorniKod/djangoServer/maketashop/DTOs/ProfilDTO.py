from maketashop.models import Korisnik

class ProfilDTO():

   def __init__(self):
      self.korisnik=Korisnik.objects.all().select_related()
   def getKorisnik(self):
      return self.korisnik