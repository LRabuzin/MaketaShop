from maketashop.models import Korisnik
from maketashop.models import Media

class ProfilPregledDTO():

    def __init__(self, id):
        self.korisnik=Korisnik.objects.all().select_related(korisnikid=id)
        self.profilna=Media.objects.all().select_related(mediaid = self.korisnik.profilnaid.mediaid)
        
    def getKorisnik(self):
        return self.korisnik

    def getProfilna(self):
        return self.profilna.putdodatoteke

