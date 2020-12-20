from maketashop.models import Korisnik

class CreditCardDTO():

   def __init__(self,email):
      self.korisnik=Korisnik.objects.get(email=email)

   def getIme(self):
      return self.korisnik.ime

   def getPrezime(self):
      return self.korisnik.prezime

   def getEmail(self):
      return self.korisnik.email

   def getAdresa(self):
      return self.korisnik.adresa

   def getKKPaypal(self):
      return self.korisnik.kkPaypal

   def getKKImePrezime(self):
      return self.korisnik.kkimeprezime

   def getKKbroj(self):
      return self.korisnik.kkbroj

   def getKKIstek(self):
      return self.korisnik.kkistek