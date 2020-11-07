from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from ..forms import PrivacyForm
from maketashop.models import Korisnik

class Profil(View):
    template_name ="maketashop/profil.html"
    def get(self, request):
        # <view logic>
        korisnik = Korisnik.objects.get(email=request.session['user'])

        data = {'address' : korisnik.adresaprivatna,
                'register_date' : korisnik.datumregistracijeprivatan,
                'birth_date' : korisnik.rodendanprivatan}
                #picture
                #surname
                #email
        form = PrivacyForm(data)

        return render(request, self.template_name, {
            'title': "profil", 
            'link_active': "profil", 
            'empty_head': False,
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
            #picture
            #surname
            #email
            korisnik = Korisnik.objects.get(email=request.session['user'])
            korisnik.adresaprivatna = adresaprivatna
            korisnik.datumregistracijeprivatan = registerprivatan
            korisnik.rodendanprivatan = rodendanprivatan
            korisnik.save()

            return HttpResponseRedirect(reverse('profil'))