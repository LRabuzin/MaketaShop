from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.models import Interakcija
from maketashop.models import Maketa
from maketashop.models import Napravljenaod
from maketashop.models import Korisnik
from ..forms import AdminCijenaForm
from maketashop.DTOs.InterakcijaMaketaDTO import InterakcijaMaketaDTO

class InterakcijaMaketa(View):
    template_name ="maketashop/interakcijaMaketa.html"
    def get(self, request, id):
        if 'user' not in request.session: 
            return HttpResponseRedirect(reverse('login'))
        else:
            user = Korisnik.objects.select_related().get(email = request.session['user'])
            if user.jeadmin:
               form = AdminCijenaForm()
               return render(request, self.template_name, {
                  'title': "interakcijaMaketa", 
                  'link_active': "interakcijaMaketa", 
                  'empty_head': False,
                  'InterakcijaMaketaDTO' : InterakcijaMaketaDTO(id), 
                  'jeAdmin' : user.jeadmin,
                  'form' : form,
                  'session': request.session
                  })
            else:
                interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
                if user == interakcija.korisnikid:
                    return render(request, self.template_name, {
                    'title': "interakcijaTema", 
                    'link_active': "interakcijaTema", 
                    'empty_head': False,
                    'InterakcijaMaketaDTO' : InterakcijaMaketaDTO(id), 
                    'session': request.session
                    })
                
                return HttpResponseRedirect(reverse('index'))
    def post(self, request, id):
      user = Korisnik.objects.select_related().get(email = request.session['user'])
      if user.jeadmin:
         form = AdminCijenaForm(request.POST)
         if form.is_valid():
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            maketa = Maketa.objects.select_related().get(maketaid = interakcija.maketaid.maketaid)
            napravljenaOd = Napravljenaod.objects.select_related().get(maketaid = interakcija.maketaid.maketaid)
            napravljenaOd.cijena = form.cleaned_data['custom_cijena']
            napravljenaOd.save()
            return HttpResponseRedirect(self.request.path_info)
      else:
         if request.POST.get("approve") == '1':
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            interakcija.interakcijaotvorena = False
            maketa = Maketa.objects.select_related().get(maketaid = interakcija.maketaid.maketaid)
            maketa.prihvacena = True
            maketa.save()
            interakcija.save()
         else:
            interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
            interakcija.interakcijaotvorena = False
            maketa = Maketa.objects.select_related().get(maketaid = interakcija.maketaid.maketaid)
            maketa.prihvacena = False
            maketa.save()
            interakcija.save()
         return HttpResponseRedirect(self.request.path_info)