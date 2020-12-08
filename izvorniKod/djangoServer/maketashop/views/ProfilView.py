from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from ..forms import PrivacyForm
from maketashop.models import Korisnik
from maketashop.DTOs.ProfilDTO import ProfilDTO

class Profil(View):
    template_name ="maketashop/profil.html"
    def get(self, request):
        # <view logic>
        korisnik = getKorisnik()

        data = {'address' : korisnik.getAdresaPrivatna(),
                'register_date' : korisnik.getDatumRegistracijePrivatan(),
                'birth_date' : korisnik.getRodendanPrivatan(),
                'pic' : korisnik.getSlikaPrivatna(),
                'name_surname' : korisnik.getImePrezimePrivatno(),
                'email' : korisnik.getEmailPrivatan()}
        form = PrivacyForm(data)

        return render(request, self.template_name, {
            'title': "profil", 
            'link_active': "profil", 
            'empty_head': False,
            'ProfilDTO' : ProfilDTO(),
            'form' : form,
            'baza_data': korisnik,
            'session': request.session
            })

    def post(self, request):
        # <view logic>
        form = PrivacyForm(request.POST)
        if form.is_valid():
            adresaprivatna = form.cleaned_data['address']
            registerprivatan = form.cleaned_data['register_date']
            rodendanprivatan = form.cleaned_data['birth_date']
            slikaprivatna = form.cleaned_data['pic']
            imeprezimeprivatno = form.cleaned_data['name_surname']
            emailprivatan = form.cleaned_data['email']
            korisnik = Korisnik.objects.get(email=request.session['user'])
            korisnik.adresaprivatna = adresaprivatna
            korisnik.datumregistracijeprivatan = registerprivatan
            korisnik.rodendanprivatan = rodendanprivatan
            korisnik.slikaprivatna = slikaprivatna
            korisnik.imeprezimeprivatno = imeprezimeprivatno
            korisnik.emailprivatan = emailprivatan
            korisnik.save()

            return HttpResponseRedirect(reverse('profil'))