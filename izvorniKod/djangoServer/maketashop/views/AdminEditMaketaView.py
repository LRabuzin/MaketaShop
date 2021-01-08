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


class AdminEditMaketa(View):
   template_name ="maketashop/adminEditMaketa.html"

   def get(self, request, id):
      # <view logic>
      
      if 'user' not in request.session:
         messages.add_message(request, messages.ERROR, 'Potreban je login.')
         return HttpResponseRedirect(reverse('login'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if not user.jeadmin:
            messages.add_message(request, messages.ERROR, 'Nemate dovoljnu razinu ovlasti.')
            return HttpResponseRedirect(reverse('index'))

         maketa = Maketa.objects.select_related().get(maketaid = id)
         
         data = {
            'ime_makete' : maketa.ime,
            'dimenzije' : maketa.dimenzije,
            'opis' : maketa.opis,
         }
         for materijal in Materijal.objects.select_related().all():
            
            if (Napravljenaod.objects.select_related().filter(maketaid = maketa.maketaid, materijalid = materijal.materijalid).exists()):
               napravljenaOd = Napravljenaod.objects.select_related().filter(maketaid = maketa.maketaid).get(materijalid = materijal.materijalid)
               data[materijal.ime] = napravljenaOd.cijena
               data[materijal.ime +"_broj_na_skladistu"] = napravljenaOd.brojuskladistu


         form = AdminMaketaForm(data)
         return render(request, self.template_name, {
         'title': "Dodaj maketu", 
         'link_active': "adminMaketa", 
         'empty_head': False,
         'adminMaketaDTO' : AdminMaketaDTO(),
         'form' : form,
         'session': request.session
         })

   def post(self, request, id):
      form = AdminMaketaForm(request.POST, request.FILES)
      if form.is_valid():

         maketa = Maketa.objects.select_related().get(maketaid = id)
         if('osnovna_slika' in request.FILES):
            media = Media()
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
            media.vrstamedije = "slika"

            nastavak = request.FILES['osnovna_slika'].name.split(".")[-1]
            putanja = handle_uploaded_file(request.FILES['osnovna_slika'], nastavak, 60)
            media.putdodatoteke = putanja
            media.save()
            maketa.mediaid = media
            maketa.save()
         for materijal in Materijal.objects.select_related().all():
            
            if form.cleaned_data.get(materijal.ime):
               cijena = form.cleaned_data.get(materijal.ime)
               if not Napravljenaod.objects.select_related().filter(maketaid = maketa.maketaid, materijalid = materijal.materijalid).exists():
                  napravljenaOd = Napravljenaod()
                  napravljenaOd.maketaid = maketa
                  napravljenaOd.materijalid = materijal
                  napravljenaOd.cijena = cijena
                  if form.cleaned_data[materijal.ime+"_broj_na_skladistu"]:
                     napravljenaOd.brojuskladistu = form.cleaned_data[materijal.ime+"_broj_na_skladistu"]
                  napravljenaOd.save()

               else:
                  napravljenaOd = Napravljenaod.objects.select_related().filter(maketaid = maketa.maketaid).get(materijalid = materijal.materijalid)
                  napravljenaOd.cijena = cijena
                  
                  if form.cleaned_data[materijal.ime+"_broj_na_skladistu"]:
                     napravljenaOd.brojuskladistu = form.cleaned_data[materijal.ime+"_broj_na_skladistu"]
                  napravljenaOd.save()

         messages.add_message(request, messages.SUCCESS, 'Maketa izmijenjena.')
         return HttpResponseRedirect(reverse('index'))


      else:
         messages.add_message(request, messages.ERROR, 'Svi uvjeti nisu zadovoljeni.')
         return HttpResponseRedirect(reverse('adminmaketa'))