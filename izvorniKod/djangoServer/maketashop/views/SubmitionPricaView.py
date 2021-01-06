from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import InteractionPostForm
from ..forms import PostForm
from maketashop.models import Interakcija
from maketashop.models import Korisnik
from maketashop.models import Prica
from maketashop.models import Media
from maketashop.models import Multimedijaprice
from django.contrib import messages

from maketashop.handle_uploaded_file import handle_uploaded_file
from maketashop.handle_uploaded_text import handle_uploaded_text


class SubmitionPrica(View):
   template_name ="maketashop/interactionPost.html"

   def get(self, request):
      # <view logic>

      #kod ako nije dozvoljen pristup korisniku
      if 'user' in request.session:
         if Korisnik.objects.filter(email=request.session['user']).exists():
            if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
               return HttpResponseRedirect(reverse('logout'))

      formUser = InteractionPostForm()
      formAdmin = PostForm()
      if 'user' not in request.session:
         messages.add_message(request, messages.ERROR, 'Potreban je login.')
         return HttpResponseRedirect(reverse('login'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if user.jeadmin:
            return render(request, self.template_name, {
            'title': "Sastavljanje priče", 
            'link_active': "submitionPrica", 
            'empty_head': False,
            'form' : formAdmin,
            'jeAdmin' : user.jeadmin,
            'session': request.session
            })

         return render(request, self.template_name, {
         'title': "Sastavljanje priče", 
         'link_active': "submitionPrica", 
         'empty_head': False,
         'form' : formUser,
         'jeAdmin' : user.jeadmin,
         'session': request.session
         })

   def post(self, request):

      user = Korisnik.objects.select_related().get(email = request.session['user'])
   
      if user.jeadmin:
         form = PostForm(request.POST, request.FILES)
      else:
         form = InteractionPostForm(request.POST, request.FILES)

      if form.is_valid():
         brojac = 0
         prica = Prica()
         prica.naslovprice = form.cleaned_data['naslovprice']
         prica.autorid = Korisnik.objects.select_related().get(email = request.session['user'])
         prica.predloziotemuid = None

         if user.jeadmin:
            prica.objavljena = True

         prica.save()
         if form.cleaned_data['text1'] :
            putanja = handle_uploaded_text(form.cleaned_data['text1'],brojac)

            media = Media()
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
               
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id;
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
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
               
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
               
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
               
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
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
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1
            media.mediaid = next_id
            media.vrstamedije = "tekst"
            media.putdodatoteke = putanja
            media.save()

            multimedija = Multimedijaprice()
            multimedija.pricaid = prica
            multimedija.mediaid = media
            brojac += 1
            multimedija.poredakuprici = brojac

            multimedija.save()
         
         

         if not user.jeadmin:
            interakcija = Interakcija()
            interakcija.korisnikid = Korisnik.objects.select_related().get(email = request.session['user'])
            interakcija.naslovinterakcije = form.cleaned_data['naslov_interakcije']
            interakcija.vrstainterakcije = "prica"
            interakcija.pricaid = prica
            interakcija.save()
      messages.add_message(request, messages.SUCCESS, 'Zahtjev poslan.')
      return HttpResponseRedirect(reverse('inbox'))
