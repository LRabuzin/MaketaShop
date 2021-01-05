from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.urls import reverse
from maketashop.DTOs.WebShopDTO import WebShopDTO
from maketashop.DTOs.CartDTO import CartDTO
from maketashop.models import Napravljenaod
from maketashop.models import Materijal, Korisnik


class WebShop(View):
    template_name ="maketashop/WebShop.html"
    def get(self, request):

        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))

        return render(request, self.template_name, {
            'title': "webshop", 
            'link_active': "webshop", 
            'empty_head': False,
            'webShopDTO': WebShopDTO(),
            'session': request.session
            })

    def post(self, request):
        if 'idMaketa' in request.POST:
            maketaId = int(request.POST['idMaketa'])
            materijal = request.POST['materijal']
            #cijena = float(request.POST['cijena'])
            cijena = float(Napravljenaod.objects.get(materijalid=Materijal.objects.get(ime=materijal), maketaid=maketaId).cijena)
            
            if not 'cart' in request.session:
                request.session['cart']=CartDTO()
            cart = request.session['cart']
            cart.addMaketa(maketaId, materijal, cijena, 1)
            request.session['cart']=cart
        return HttpResponseRedirect(self.request.path_info)