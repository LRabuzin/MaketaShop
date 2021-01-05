from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from maketashop.models import Korisnik
from django.urls import reverse
from django.views.generic import View
from ..forms import SignupForm
from datetime import date
from django.contrib import messages

class Signup(View):
    template_name="maketashop/signup.html"

    def get(self, request):
        form = SignupForm()
        if 'user' not in request.session:
            return render(request, self.template_name, {
                'title': "signup", 
                'link_active': "signup", 
                'empty_head': True,
                'form':form,
                'session': request.session
                })
        else:
            return HttpResponseRedirect(reverse('index'))

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            ime = form.cleaned_data['name']
            prezime = form.cleaned_data['surname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            lozinka1 = form.cleaned_data['pass1']
            lozinka2 = form.cleaned_data['pass2']
            adresa = form.cleaned_data['adress']
            #brojKartice = form.cleaned_data['cardNumber']
            razinaautoriteta = 1
            if lozinka1 == lozinka2:
                if Korisnik.objects.filter(email=email).exists():
                    messages.add_message(request, messages.ERROR, 'Korisnik s tim mailom već postoji!')
                    return HttpResponseRedirect(reverse('signup'))
                if Korisnik.objects.filter(korisnickoime=username).exists():
                    messages.add_message(request, messages.ERROR, 'Korisnik s tim korisničkim imenom već postoji!')
                    return HttpResponseRedirect(reverse('signup'))
                else:
                    korisnik = Korisnik()
                    korisnik.ime = ime
                    korisnik.prezime = prezime
                    korisnik.korisnickoime = username
                    korisnik.email = email
                    korisnik.lozinka = lozinka1
                    korisnik.adresa = adresa
                    #korisnik.brojracuna = brojKartice
                    korisnik.razinaautoriteta = razinaautoriteta
                    korisnik.save()

                    request.session['user'] = korisnik.email
                    request.session['admin'] = False
                    messages.add_message(request, messages.SUCCESS, 'Registracija uspješna!')
                    return HttpResponseRedirect(reverse('index'))
        messages.add_message(request, messages.ERROR, 'Registracija neuspješna!')
        return HttpResponseRedirect(reverse('signup'))
