from maketashop.models import Korisnik

class AULDTO():

    def __init__(self, request):
        self.ovlast = Korisnik.objects.select_related().get(email = request.session['user']).jeadmin
        self.korisnici = Korisnik.objects.all().select_related()
        self.searchterm = ""
    
    def getKorisnici(self):
        return self.korisnici
    
    def getOvlast(self):
        return self.ovlast

    def getSearchTerm(self):
        return self.searchterm

        
