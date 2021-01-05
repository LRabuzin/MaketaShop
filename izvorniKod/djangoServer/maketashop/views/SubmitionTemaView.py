from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from datetime import datetime
from ..forms import InteractionThemeForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Tema
#from maketashop.handle_uploaded_file import handle_uploaded_file

class SubmitionTema(View):
   template_name ="maketashop/tema.html"

   def get(self, request):
      # <view logic>

      #kod ako nije dozvoljen pristup korisniku
      if Korisnik.objects.filter(email=request.session['user']).exists():
         if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
            return HttpResponseRedirect(reverse('logout'))

      form = InteractionThemeForm()
      if 'user' not in request.session:
         return HttpResponseRedirect(reverse('index'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if user.jeadmin:
            return HttpResponseRedirect(reverse('index'))
         
         return render(request, self.template_name, {
         'title': "submitionTema", 
         'link_active': "submitionTema", 
         'empty_head': False,
         'form' : form,
         'session': request.session
         })

   def post(self, request):
      form = InteractionThemeForm(request.POST)
      if form.is_valid():

         tema = Tema()
         tema.ime = form.cleaned_data['ime_teme']
         tema.tekstteme = form.cleaned_data['tekst_teme']

         tema.save()
         interakcija = Interakcija()
         interakcija.korisnikid = Korisnik.objects.select_related().get(email = request.session['user'])
         interakcija.naslovinterakcije = form.cleaned_data['naslov_interakcije']
         interakcija.vrstainterakcije = "tema"
         interakcija.temaid = tema
         interakcija.save()


         return HttpResponseRedirect(reverse('index'))
