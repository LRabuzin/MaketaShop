from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Korisnik

class Profil(View):
    template_name ="maketashop/profil.html"
    def get(self, request):
        # <view logic>

        korisnik = Korisnik.objects.get(email=request.session['user'])
        return render(request, self.template_name, {
            'title': "profil", 
            'link_active': "profil", 
            'empty_head': request.session['empty_head'],
            'baza_data': korisnik
            })