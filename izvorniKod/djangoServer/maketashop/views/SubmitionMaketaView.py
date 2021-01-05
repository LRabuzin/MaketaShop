from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import InteractionMaketaForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Maketa
from maketashop.models import Vrstamakete
from maketashop.models import Media
from maketashop.models import Napravljenaod
from django.contrib import messages


class SubmitionMaketa(View):
   template_name ="maketashop/interactionMaketa.html"

   def get(self, request):
      # <view logic>

      #kod ako nije dozvoljen pristup korisniku
      if 'user' in request.session:
         if Korisnik.objects.filter(email=request.session['user']).exists():
            if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
               return HttpResponseRedirect(reverse('logout'))

      form = InteractionMaketaForm()
      if 'user' not in request.session:
         messages.add_message(request, messages.ERROR, 'Obavezan login.')
         return HttpResponseRedirect(reverse('login'))
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
         
         media = Media.objects.select_related().get(mediaid = 1)

         maketa.mediaid = media
         maketa.save()

         napravljenaOd = Napravljenaod()
         napravljenaOd.maketaid = maketa
         napravljenaOd.materijalid = form.cleaned_data['materijal']
         napravljenaOd.cijena = None
         napravljenaOd.brojuskladistu = 1
         napravljenaOd.save()

         interakcija = Interakcija()
         interakcija.korisnikid = Korisnik.objects.select_related().get(email = request.session['user'])
         interakcija.naslovinterakcije = form.cleaned_data['naslov_interakcije']
         interakcija.vrstainterakcije = "maketa"
         interakcija.maketaid = maketa
         interakcija.save()

      messages.add_message(request, messages.SUCCESS, 'Zahtjev poslan.')
      return HttpResponseRedirect(reverse('inbox'))
