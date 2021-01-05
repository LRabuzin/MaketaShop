from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.CartDTO import CartDTO
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from maketashop.models import Napravljenaod
from maketashop.models import Materijal, Korisnik

class Cart(View):
    template_name ="maketashop/cart.html"
    def get(self, request):
        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))
        if 'cart' in request.session:
            Cart=request.session['cart']
        else:
            Cart=CartDTO()
        return render(request, self.template_name, {
            'title': "Košarica", 
            'link_active': "cart", 
            'empty_head': False,
            'cartDTO' : Cart,
            'session': request.session
            })

    def post(self, request):
        if 'metoda' in request.POST:
                if 'cart' in request.session:
                    cart = request.session['cart']
                    maketaId = int(request.POST['idMaketa'])
                    materijal = request.POST['materijal']
                    #cijena = float(request.POST['cijena'])
                    cijena = float(Napravljenaod.objects.get(materijalid=Materijal.objects.get(ime=materijal), maketaid=maketaId).cijena)
                    #brisanje sve od jednog itema
                    if request.POST['metoda'] == '1':
                        cart.removeSveOdMaketa(maketaId, materijal, cijena)
                    
                    #dodavanje jednog itema
                    elif request.POST['metoda'] == '2':
                        cart.addMaketa(maketaId, materijal, cijena, 1)
                    
                    #micanje jednog itema
                    elif request.POST['metoda'] == '3':
                        cart.removeMaketa(maketaId, materijal, cijena, 1)
                    
                    request.session['cart'] = cart
        return HttpResponseRedirect(self.request.path_info)