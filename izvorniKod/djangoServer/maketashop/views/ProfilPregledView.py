from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.ProfilPregledDTO import ProfilPregledDTO
from maketashop.models import Korisnik

class ProfilPregled(View):
    template_name ="maketashop/profilPregled.html"
    
    def get(self, request, id):
        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))
        
            if id == Korisnik.objects.get(email=request.session['user']).korisnikid:
                return HttpResponseRedirect(reverse('profil'))

        return render(request, self.template_name, {
            'title': "Pregled profila", 
            'link_active': "profilPregled", 
            'empty_head': False,
            'session': request.session,
            'ProfilPregledDTO' : ProfilPregledDTO(id)
            })
