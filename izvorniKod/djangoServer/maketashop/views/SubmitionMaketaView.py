from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import InteractionMaketaForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Maketa
from maketashop.models import Vrstamakete


class SubmitionMaketa(View):
   template_name ="maketashop/interactionMaketa.html"

   def get(self, request):
      # <view logic>
      form = InteractionMaketaForm()
      if 'user' not in request.session:
         return HttpResponseRedirect(reverse('index'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if user.jeadmin:
            return HttpResponseRedirect(reverse('index'))

         return render(request, self.template_name, {
         'title': "submitionMaketa", 
         'link_active': "submitionMaketa", 
         'empty_head': False,
         'form' : form,
         'session': request.session
         })

   def post(self, request):
      form = InteractionMaketaForm(request.POST)
      if form.is_valid():

         vrsta = Vrstamakete.objects.select_related().get(ime = 'custom')


         maketa = Maketa()
         maketa.ime = form.cleaned_data['ime_makete']
         maketa.dimenzije = form.cleaned_data['dimenzije']
         maketa.opis = form.cleaned_data['opis']
         maketa.vrsta = vrsta
         maketa.save()

         interakcija = Interakcija()
         interakcija.korisnikid = Korisnik.objects.select_related().get(email = request.session['user'])
         interakcija.naslovinterakcije = form.cleaned_data['naslov_interakcije']
         interakcija.vrstainterakcije = "maketa"
         interakcija.maketaid = maketa
         interakcija.save()


      return HttpResponseRedirect(reverse('index'))
