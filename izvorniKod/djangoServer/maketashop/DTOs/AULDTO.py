from maketashop.models import Korisnik

class AULDTO():

    def __init__(self, request):
        self.ovlast = Korisnik.objects.select_related().get(email = request.session['user'])
        self.korisnici= Korisnik.objects.all().select_related()
    
    def getKorisnici(self):
        return self.korisnici
    
    def getOvlast(self):
        self.ovlast

        