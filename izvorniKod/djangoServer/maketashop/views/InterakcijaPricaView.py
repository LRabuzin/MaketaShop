from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Prica
from maketashop.DTOs.InterakcijaPricaDTO import InterakcijaPricaDTO
from django.contrib import messages

class InterakcijaPrica(View):
    template_name ="maketashop/interakcijaPrica.html"
    def get(self, request, id):
        if 'user' not in request.session: 
            messages.add_message(request, messages.ERROR, 'Potreban je login.')
            return HttpResponseRedirect(reverse('login'))
        else:
            #kod ako nije dozvoljen pristup korisniku
            if 'user' in request.session:
               if Korisnik.objects.filter(email=request.session['user']).exists():
                  if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                     return HttpResponseRedirect(reverse('logout'))

            user = Korisnik.objects.select_related().get(email = request.session['user'])
            if user.jeadmin:
               return render(request, self.template_name, {
                  'title': "Interakcija (priča)", 
                  'link_active': "interakcijaPrica", 
                  'empty_head': False,
                  'InterakcijaPricaDTO' : InterakcijaPricaDTO(id), 
                  'jeAdmin' : user.jeadmin,
                  'session': request.session
                  })
            else:
                interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
                if user == interakcija.korisnikid:
                    return render(request, self.template_name, {
                    'title': "Interakcija (priča)", 
                    'link_active': "interakcijaPrica", 
                    'empty_head': False,
                    'InterakcijaPricaDTO' : InterakcijaPricaDTO(id), 
                    'session': request.session
                    })
                
                return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
      user = Korisnik.objects.select_related().get(email = request.session['user'])
      if user.jeadmin:
         if request.POST.get("approve") == '1':
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            prica = Prica.objects.select_related().get(pricaid = interakcija.pricaid.pricaid)
            prica.objavljena = True
            interakcija.interakcijaotvorena = False
            prica.save()
            interakcija.save()
         else:
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            interakcija.interakcijaotvorena = False
            interakcija.save()
         return HttpResponseRedirect(self.request.path_info)
      else:
         messages.add_message(request, messages.ERROR, 'Nemate dovoljnu razinu ovlasti.')
         return HttpResponseRedirect(reverse('index'))