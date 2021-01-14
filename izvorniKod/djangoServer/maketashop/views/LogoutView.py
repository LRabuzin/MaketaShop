from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from maketashop.models import Korisnik
from django.contrib import messages

class Logout(View):
    template_name ="logout"
    def get(self, request):
      if 'user' in request.session:
         if Korisnik.objects.filter(email=request.session['user']).exists():
            if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
               messages.add_message(request, messages.ERROR, 'Pristup ovome računu nije dozvoljen!')
         del request.session['user']
         if 'cart' in request.session:
            del request.session['cart']
         del request.session['admin']
         return HttpResponseRedirect(reverse('index'))
      else:
         return HttpResponseRedirect(reverse('login'))