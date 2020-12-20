from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.ProfilDTO import ProfilDTO
from maketashop.DTOs.CreditCardDTO import CreditCardDTO

from ..forms import PlacanjeForm

class Checkout(View):
    template_name ="maketashop/checkout.html"
    def get(self, request):
        # <view logic>
        email = request.session.get('user')
        if email:
            korisnik = ProfilDTO(email)
            kartica = CreditCardDTO(email)

            data = {
                'ime' : korisnik.getIme(),
                'prezime' : korisnik.getPrezime(),
                'adresa' : korisnik.getAdresa(),
                'email' : korisnik.getEmail(),
                'ime_na_kartici': kartica.getKKImePrezime(),
                # 'paypal_bool': kartica.getKKPaypal(),
                'broj_kartice': kartica.getKKBroj(),
                'istek_kartice': kartica.getKKIstek(),
                'cvv': "" 
            }
            
            form = PlacanjeForm(data)
            
            return render(request, self.template_name, {
                'title': "checkout",
                'link_active' : "checkout",
                'empty_head' : False,
                'form' : form,
                'session' : request.session
            })

        else:

            data = {
                'ime' : "",
                'prezime' : "",
                'adresa' : "",
                'email' : "",
                'ime_na_kartici': "",
                # 'paypal_bool': "",
                'broj_kartice': "",
                'istek_kartice': "",
                'cvv': "" 
            }

            form = PlacanjeForm(data)

            return render(request, self.template_name, {
                'title': "checkout", 
                'link_active': "checkout", 
                'empty_head': False,
                'form' : form,
                'session': request.session
            })