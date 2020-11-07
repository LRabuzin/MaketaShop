from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from maketashop.models import Korisnik
from django.urls import reverse
from django.views.generic import View


class Signup(View):
    template_name="maketashop/signup.html"

    def get(self, request):
        if 'user' not in request.session:
            return render(request, self.template_name, {
                'title': "signup", 
                'link_active': "signup", 
                'empty_head': False
                })
        else:
            return HttpResponseRedirect(reverse('index'))
    def post(self, request):
        if Korisnik.objects.filter(email=request.POST.get('email')).exists():
            return HttpResponseRedirect(reverse('signup'))
        else:
            korisnik = Korisnik()
            korisnik.ime = request.POST.get('ime')
            korisnik.prezime = request.POST.get('prezime')
            korisnik.email = request.POST.get('email')
            korisnik.lozinka = request.POST.get('pass1')
            korisnik.razinaautoriteta = 1
            korisnik.save()

            request.session['user'] = korisnik.email
            request.session['empty_head'] = True
            return HttpResponseRedirect(reverse('index'))