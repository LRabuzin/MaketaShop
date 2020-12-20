from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from datetime import datetime
from ..forms import InteractionMaketaForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Maketa
#from maketashop.handle_uploaded_file import handle_uploaded_file

class SubmitionMaketa(View):
   template_name ="maketashop/interactionMaketa.html"

   def get(self, request):
      # <view logic>
      form = InteractionMaketaForm()
      if 'user' not in request.session:
         return HttpResponseRedirect(reverse('index'))
      else:
         return render(request, self.template_name, {
         'title': "submitionMaketa", 
         'link_active': "submitionMaketa", 
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
         interakcija.naslovinterakcije = form.cleaned_data['tekst_teme']
         interakcija.vrstainterakcije = "tema"
         interakcija.temaid = tema
         interakcija.save()


         return HttpResponseRedirect('submition')
