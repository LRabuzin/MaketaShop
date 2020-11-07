from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from ..forms import PrivacyForm

class Profil(View):
    template_name ="maketashop/profil.html"
    def get(self, request):
        # <view logic>
        form = PrivacyForm()
        
        korisnik = Korisnik.objects.get(email=request.session['user'])
        return render(request, self.template_name, {
            'title': "profil", 
            'link_active': "profil", 
            'empty_head': False,
            'form' : form,
            'baza_data': korisnik
            })