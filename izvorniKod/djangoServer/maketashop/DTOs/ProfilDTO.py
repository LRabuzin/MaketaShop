from maketashop.models import Korisnik

class ProfilDTO():

   def __init__(self, korisnikId):
      self.korisnik=Korisnik.objects.get(korisnikId)

   def getEmail(self):
      return self.korisnik.email

   def getKorisnickoIme(self):
      return self.korisnik.korisnickoime

   def getAdresa(self):
      return self.korisnik.adresa

   def getRodendan(self):
      return self.korisnik.rodendan

   def getDatumRegistracije(self):
      return self.korisnik.datumregistracije

   def getIme(self):
      return self.korisnik.ime

   def getPrezime(self):
      return self.korisnik.prezime

   def getSlika(self):
      return self.korisnik.profilnaid.putdodatoteke
      
   def getKorisnik(self):
      return self.korisnik.korisnickoime
