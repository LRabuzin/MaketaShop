from maketashop.models import Korisnik

class ProfilDTO():

   def __init__(self, email):
      self.korisnik=Korisnik.objects.get(email=email)

   def getEmail(self):
      return self.korisnik.email

   def getKorisnickoIme(self):
      return self.korisnik.korisnickoime

   def getAdresa(self):
      return self.korisnik.adresa

#   def getRodendan(self):
#      return self.korisnik.rodendan

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

   def getAdresaPrivatna(self):
      return self.korisnik.adresaprivatna
	
   #def getRodendanPrivatan(self):
   #   return self.korisnik.rodendanprivatan
	
   def getDatumRegistracijePrivatan(self):
      return self.korisnik.datumregistracijeprivatan
	
   def getSlikaPrivatna(self):
      return self.korisnik.slikaprivatna
	
   def getImePrezimePrivatno(self):
      return self.korisnik.imeprezimeprivatno
	
   def getEmailPrivatan(self):
      return self.korisnik.emailprivatan
