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
from maketashop.DTOs.CartDTO import CartDTO
from django.contrib import messages

class InterakcijaMaketa(View):
    template_name ="maketashop/interakcijaMaketa.html"
    def get(self, request, id):
        if 'user' not in request.session: 
         messages.add_message(request, messages.ERROR, 'Potreban je login.')
         return HttpResponseRedirect(reverse('login'))
        else:
            #kod ako nije dozvoljen pristup korisniku
            if 'user' in request.session:
               if Korisnik.objects.filter(email=request.session['user']).exists():
                  if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                     return HttpResponseRedirect(reverse('logout'))

            user = Korisnik.objects.select_related().get(email = request.session['user'])
            if user.jeadmin:
               form = AdminCijenaForm()
               return render(request, self.template_name, {
                  'title': "Interakcija (maketa)", 
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
                    'title': "Interakcija (maketa)", 
                    'link_active': "interakcijaMaketa", 
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
         interakcija = Interakcija.objects.select_related().get(interakcijaid = id)
         
         maketa = Maketa.objects.select_related().get(maketaid = interakcija.maketaid.maketaid)
         if request.POST.get("approve") == '1':

            interakcija.interakcijaotvorena = False
            maketa.prihvacena = True
            maketa.save()
            interakcija.save()
         elif request.POST.get("approve") == '0':
            interakcija.interakcijaotvorena = False
            maketa.prihvacena = False
            maketa.save()
            interakcija.save()
         elif request.POST.get("purchase") == '1':
            if not 'cart' in request.session:
               request.session['cart']=CartDTO()
            cart = request.session['cart']
            materijal = Napravljenaod.objects.get(maketaid = maketa.maketaid).materijalid.ime
            cijena = Napravljenaod.objects.get(maketaid = maketa.maketaid).cijena
            kolicina = Napravljenaod.objects.get(maketaid = maketa.maketaid).brojuskladistu
            cart.addMaketa(maketa.maketaid, materijal, cijena, kolicina)
            request.session['cart'] = cart
            return HttpResponseRedirect(reverse('cart'))
         return HttpResponseRedirect(self.request.path_info)