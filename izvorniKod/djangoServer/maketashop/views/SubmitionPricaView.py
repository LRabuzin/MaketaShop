from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import InteractionPostForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Prica
from maketashop.models import Media
from maketashop.models import Multimedijaprice

from maketashop.handle_uploaded_file import handle_uploaded_file
from maketashop.handle_uploaded_text import handle_uploaded_text


class SubmitionPrica(View):
   template_name ="maketashop/interactionPost.html"

   def get(self, request):
      # <view logic>
      form = InteractionPostForm()
      if 'user' not in request.session:
         return HttpResponseRedirect(reverse('index'))
      else:
         if request.session['user'].jeadmin:
            return HttpResponseRedirect(reverse('index'))
            
         return render(request, self.template_name, {
         'title': "submitionMaketa", 
         'link_active': "submitionMaketa", 
         'empty_head': False,
         'form' : form,
         'session': request.session
         })

   def post(self, request):
      form = InteractionPostForm(request.POST, request.FILES)

      if form.is_valid():
         brojac = 0

         prica = Prica()
         prica.naslovprice = form.cleaned_data['naslovprice']
         prica.autorid = Korisnik.objects.select_related().get(email = request.session['user'])
         prica.predloziotemuid = None
         prica.save()
         if form.cleaned_data['text1'] :
            putanja = handle_uploaded_text(form.cleaned_data['text1'],brojac)

            media = Media()
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if request.FILES.get('media1'):

            nastavak = request.FILES['media1'].name.split(".")[-1]
            putanja = handle_uploaded_file(request.FILES['media1'], nastavak, brojac)

            
            media = Media()

            if nastavak == "jpg" or nastavak == "jpeg" or nastavak == "gif" or nastavak == "png":
               media.vrstamedije = "slika"
            elif(nastavak == "mkv" or nastavak == "avi" or nastavak == "mov" or nastavak == "mp4"):
               media.vrstamedije = "video"

            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if form.cleaned_data['text2']:
            putanja = handle_uploaded_text(form.cleaned_data['text2'], brojac)

            media = Media()
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if request.FILES.get('media2') != None:

            nastavak = request.FILES['media2'].name.split(".")[-1]
            putanja = handle_uploaded_file(request.FILES['media2'], nastavak, brojac)

            
            media = Media()

            if nastavak == "jpg" or nastavak == "jpeg" or nastavak == "gif" or nastavak == "png":
               media.vrstamedije = "slika"
            elif(nastavak == "mkv" or nastavak == "avi" or nastavak == "mov" or nastavak == "mp4"):
               media.vrstamedije = "video"

            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if form.cleaned_data['text3']:
            putanja = handle_uploaded_text(form.cleaned_data['text3'], brojac)

            media = Media()
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if request.FILES.get('media3') != None:

            nastavak = request.FILES['media3'].name.split(".")[-1]
            putanja = handle_uploaded_file(request.FILES['media3'], nastavak, brojac)

            
            media = Media()

            if nastavak == "jpg" or nastavak == "jpeg" or nastavak == "gif" or nastavak == "png":
               media.vrstamedije = "slika"
            elif(nastavak == "mkv" or nastavak == "avi" or nastavak == "mov" or nastavak == "mp4"):
               media.vrstamedije = "video"

            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if form.cleaned_data['text4']:
            putanja = handle_uploaded_text(form.cleaned_data['text4'], brojac)

            media = Media()
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if request.FILES.get('media4') != None:

            nastavak = request.FILES['media4'].name.split(".")[-1]
            putanja = handle_uploaded_file(request.FILES['media4'], nastavak, brojac)

            
            media = Media()

            if nastavak == "jpg" or nastavak == "jpeg" or nastavak == "gif" or nastavak == "png":
               media.vrstamedije = "slika"
            elif(nastavak == "mkv" or nastavak == "avi" or nastavak == "mov" or nastavak == "mp4"):
               media.vrstamedije = "video"

            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         if form.cleaned_data['text5']:
            putanja = handle_uploaded_text(form.cleaned_data['text5'], brojac)

            media = Media()
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         


         interakcija = Interakcija()
         interakcija.korisnikid = Korisnik.objects.select_related().get(email = request.session['user'])
         interakcija.naslovinterakcije = form.cleaned_data['naslov_interakcije']
         interakcija.vrstainterakcije = "prica"
         interakcija.pricaid = prica
         interakcija.save()

         

      


      return HttpResponseRedirect(reverse('index'))