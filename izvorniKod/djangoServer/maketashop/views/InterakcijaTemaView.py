from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Tema
from maketashop.DTOs.InterakcijaTemaDTO import InterakcijaTemaDTO

class InterakcijaTema(View):
    template_name ="maketashop/interakcijaTema.html"
    def get(self, request, id):
        if 'user' not in request.session: 
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
                  'title': "Interakcija (tema)", 
                  'link_active': "interakcijaTema", 
                  'empty_head': False,
                  'InterakcijaTemaDTO' : InterakcijaTemaDTO(id), 
                  'jeAdmin' : user.jeadmin,
                  'session': request.session
                  })
            else:
                interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
                if user == interakcija.korisnikid:
                    return render(request, self.template_name, {
                    'title': "Interakcija (tema)", 
                    'link_active': "interakcijaTema", 
                    'empty_head': False,
                    'InterakcijaTemaDTO' : InterakcijaTemaDTO(id), 
                    'session': request.session
                    })
                
                return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
      user = Korisnik.objects.select_related().get(email = request.session['user'])
      if user.jeadmin:
         if request.POST.get("approve") == '1':
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            tema = Tema.objects.select_related().get(temaid = interakcija.temaid.temaid)
            tema.odobrena = True
            interakcija.interakcijaotvorena = False
            tema.save()
            interakcija.save()
         else:
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            interakcija.interakcijaotvorena = False
            interakcija.save()
         return HttpResponseRedirect(self.request.path_info)
      else:
         return HttpResponseRedirect(reverse('index'))
