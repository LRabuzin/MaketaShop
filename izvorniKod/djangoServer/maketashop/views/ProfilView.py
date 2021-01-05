from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from ..forms import PrivacyForm
from maketashop.models import Korisnik
from maketashop.DTOs.ProfilDTO import ProfilDTO
from maketashop.models import Media
from maketashop.handle_uploaded_file import handle_uploaded_file
from maketashop.handle_uploaded_text import handle_uploaded_text
from django.db.models import Max



class Profil(View):
    template_name ="maketashop/profil.html"
    def get(self, request):
        # <view logic>
        email = request.session['user']
        korisnik = ProfilDTO(email)

        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))

        data = {'address' : korisnik.getAdresaPrivatna(),
                'register_date' : korisnik.getDatumRegistracijePrivatan(),
                'birth_date' : korisnik.getRodendanPrivatan(),
                'pic' : korisnik.getSlikaPrivatna(),
                'name_surname' : korisnik.getImePrezimePrivatno(),
                'email' : korisnik.getEmailPrivatan()}
        form = PrivacyForm(data)

        return render(request, self.template_name, {
            'title': "Profil", 
            'link_active': "profil", 
            'empty_head': False,
            'ProfilDTO' : ProfilDTO(email),
            'form' : form,
            'baza_data': korisnik,
            'session': request.session
            })

    def post(self, request):
        korisnik = Korisnik.objects.get(email=request.session['user'])
        
        if request.FILES.get('profilna'):
            brojac = 0
            nastavak = request.FILES['profilna'].name.split(".")[-1]
            putanja = handle_uploaded_file( request.FILES['profilna'], nastavak, brojac)
            #putanja = putanja.replace("maketashop/static", "");

            media = Media();

            if nastavak == "jpg" or nastavak == "jpeg" or nastavak == "gif" or nastavak == "png":
                media.vrstamedije = "slika"
            elif(nastavak == "mkv" or nastavak == "avi" or nastavak == "mov" or nastavak == "mp4"):
                media.vrstamedije = "video"
                
            next_id = Media.objects.order_by('-mediaid').first().mediaid + 1

            media.mediaid = next_id;
            media.putdodatoteke = putanja
            media.save()
            korisnik.profilnaid = media;
        
        # <view logic>
        form = PrivacyForm(request.POST)
        if form.is_valid():          
            
            adresaprivatna = form.cleaned_data['address']
            registerprivatan = form.cleaned_data['register_date']
            rodendanprivatan = form.cleaned_data['birth_date']
            # slikaprivatna = form.cleaned_data['pic']
            imeprezimeprivatno = form.cleaned_data['name_surname']
            emailprivatan = form.cleaned_data['email']
            korisnik.adresaprivatna = adresaprivatna
            korisnik.datumregistracijeprivatan = registerprivatan
            korisnik.rodendanprivatan = rodendanprivatan
            #korisnik.slikaprivatna = slikaprivatna
            korisnik.imeprezimeprivatno = imeprezimeprivatno
            korisnik.emailprivatan = emailprivatan
            korisnik.save()

            

            

            return HttpResponseRedirect(reverse('profil'))
