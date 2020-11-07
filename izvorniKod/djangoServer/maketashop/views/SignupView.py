from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from maketashop.models import Korisnik
from django.urls import reverse
from django.views.generic import View
from ..forms import SignupForm

class Signup(View):
    template_name="maketashop/signup.html"

    def get(self, request):
        form = SignupForm()
        if 'user' not in request.session:
            return render(request, self.template_name, {
                'title': "signup", 
                'link_active': "signup", 
                'empty_head': True,
                'form':form
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
            lozinka = form.cleaned_data['pass1']
            razinaautoriteta = 1

            if Korisnik.objects.filter(email=email).exists():
                return HttpResponseRedirect(reverse('signup'))
            else:
                korisnik = Korisnik()
                korisnik.ime = ime
                korisnik.prezime = prezime
                korisnik.korisnickoime = username
                korisnik.email = email
                korisnik.lozinka = lozinka
                korisnik.razinaautoriteta = razinaautoriteta
                korisnik.save()

                request.session['user'] = korisnik.email
                return HttpResponseRedirect(reverse('index'))