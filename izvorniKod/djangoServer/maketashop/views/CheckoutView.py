from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.ProfilDTO import ProfilDTO
from maketashop.DTOs.CreditCardDTO import CreditCardDTO
from maketashop.models import Transakcija, Korisnik, Maketakupljena, Materijal
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
                'paypal_bool': 'paypal' if kartica.getKKPaypal() else 'kreditnaKartica',
                'broj_kartice': kartica.getKKBroj(),
                'istek_kartice': kartica.getKKIstek(),
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
            form = PlacanjeForm()

            return render(request, self.template_name, {
                'title': "checkout", 
                'link_active': "checkout", 
                'empty_head': False,
                'form' : form,
                'session': request.session
            })

    def post(self, request):
        form = PlacanjeForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['ime']
            prezime = form.cleaned_data['prezime']
            adresa = form.cleaned_data['adresa']
            email = form.cleaned_data['email']
            ime_na_kartici = form.cleaned_data['ime_na_kartici']
            broj_kartice = form.cleaned_data['broj_kartice']
            istek_kartice = form.cleaned_data['istek_kartice']
            paypal_bool = form.cleaned_data['paypal_bool']

            cart = request.session['cart']
            ukupaniznos = cart.getUkupno()
            
            if 'user' in request.session:
                korisnik = Korisnik.objects.get(email=request.session['user'])
                if(korisnik.kkimeprezime!=ime_na_kartici):
                    korisnik.kkimeprezime=ime_na_kartici

                if(korisnik.kkpaypal == False):
                    if(paypal_bool=='paypal'):
                        korisnik.kkpaypal=True
                else:
                    if(paypal_bool=='kreditnaKartica'):
                        korisnik.kkpaypal=False
                
                if(korisnik.kkbroj != broj_kartice):
                    korisnik.kkbroj = broj_kartice

                if(korisnik.kkistek != istek_kartice):
                    korisnik.kkistek = istek_kartice

                korisnik.save()

            novaTransakcija = Transakcija()
            novaTransakcija.ime = ime
            novaTransakcija.prezime = prezime
            novaTransakcija.adresa = adresa
            novaTransakcija.brojracuna = broj_kartice
            novaTransakcija.ukupaniznos = ukupaniznos
            if 'user' in request.session:
                novaTransakcija.korisnik = Korisnik.objects.get(email=request.session['user'])
            novaTransakcija.save()

            for maketa,kol in cart.getCart().items():
                maketakupljena = Maketakupljena()
                maketakupljena.maketaid = maketa.getMaketa()
                maketakupljena.materijalid = Materijal.objects.get(ime=maketa.getMaterijal())
                maketakupljena.kolicina = kol
                maketakupljena.transakcijaid = novaTransakcija
                maketakupljena.save()
            
            if 'cart' in request.session:
                del request.session['cart']

            return HttpResponseRedirect(reverse('transakcije'))
        return HttpResponseRedirect(self.request.path_info)