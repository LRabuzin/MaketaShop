from maketashop.models import Korisnik
from maketashop.models import Tema
from maketashop.models import Interakcija
from maketashop.models import Korisnik

class InboxDTO():

      def __init__(self, mail):
         self.user = Korisnik.objects.get(email = mail)

         if(self.user.jeadmin):
            self.interakcije = Interakcija.objects.all().select_related().order_by('-datumstvorena')
         else:
            self.interakcije = Interakcija.objects.select_related().filter(korisnikid = self.user.korisnikid).order_by('-datumstvorena')
      
      def getInterakcije(self):
         return self.interakcije

         



         
