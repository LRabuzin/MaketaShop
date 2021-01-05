from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import AdminMaketaForm
from maketashop.handle_uploaded_file import handle_uploaded_file
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Maketa
from maketashop.models import Vrstamakete
from maketashop.models import Materijal
from maketashop.models import Media
from maketashop.models import Napravljenaod
from django.contrib import messages
from maketashop.DTOs.AdminMaketaDTO import AdminMaketaDTO


class AdminMaketa(View):
   template_name ="maketashop/adminMaketa.html"

   def get(self, request):
      # <view logic>
      form = AdminMaketaForm()
      if 'user' not in request.session:
         return HttpResponseRedirect(reverse('login'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if not user.jeadmin:
            return HttpResponseRedirect(reverse('index'))
         return render(request, self.template_name, {
         'title': "Dodaj maketu", 
         'link_active': "adminMaketa", 
         'empty_head': False,
         'adminMaketaDTO' : AdminMaketaDTO(),
         'form' : form,
         'session': request.session
         })

   def post(self, request):
      form = AdminMaketaForm(request.POST, request.FILES)
      if form.is_valid():

         vrsta = Vrstamakete.objects.select_related().get(ime = 'webshop')


         maketa = Maketa()
         maketa.ime = form.cleaned_data['ime_makete']
         maketa.dimenzije = form.cleaned_data['dimenzije']
         maketa.opis = form.cleaned_data['opis']
         maketa.vrsta = vrsta
         
         media = Media()
         next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
         media.mediaid = next_id
         media.vrstamedije = "slika"

         nastavak = request.FILES['osnovna_slika'].name.split(".")[-1]
         putanja = handle_uploaded_file(request.FILES['osnovna_slika'], nastavak, 42)
         media.putdodatoteke = putanja
         media.save()

         maketa.mediaid = media
         maketa.prihvacena = True
         maketa.save()



         for materijal in Materijal.objects.select_related().all():
            cijena = form.cleaned_data[materijal.ime]
            if cijena:
               napravljenaOd = Napravljenaod()
               napravljenaOd.maketaid = maketa
               
               napravljenaOd.materijalid = materijal
               napravljenaOd.cijena = cijena
               napravljenaOd.brojuskladistu = form.cleaned_data['broj_na_skladistu']
               napravljenaOd.save()


      messages.add_message(request, messages.SUCCESS, 'Maketa dodana u webshop.')
      return HttpResponseRedirect(reverse('index'))