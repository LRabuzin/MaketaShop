from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.DTOs.InterakcijaTemaDTO import InterakcijaTemaDTO

class InterakcijaTema(View):
    template_name ="maketashop/interakcijaTema.html"
    def get(self, request, id):
        if 'user' not in request.session: 
            return HttpResponseRedirect(reverse('login'))
        else:
            user = Korisnik.objects.select_related().get(email = request.session['user'])
            if user.jeadmin:
               return render(request, self.template_name, {
                  'title': "interakcija", 
                  'link_active': "interakcija", 
                  'empty_head': False,
                  'InterakcijaDTO' : InterakcijaTemaDTO(id), 
                  'jeAdmin' : user.jeadmin,
                  'session': request.session
                  })
            else:
                interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
                if user == interakcija.korisnikid:
                    return render(request, self.template_name, {
                    'title': "interakcija", 
                    'link_active': "interakcija", 
                    'empty_head': False,
                    'InterakcijaTemaDTO' : InterakcijaTemaDTO(id), 
                    'session': request.session
                    })
                
                return HttpResponseRedirect(reverse('index'))