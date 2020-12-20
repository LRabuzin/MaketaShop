from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified
from django.urls import reverse
from maketashop.DTOs.WebShopDTO import WebShopDTO
from maketashop.DTOs.CartDTO import CartDTO

class WebShop(View):
    template_name ="maketashop/WebShop.html"
    def get(self, request):

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
            cijena = float(request.POST['cijena'])
            materijal = request.POST['materijal']

            if not 'cart' in request.session:
                request.session['cart']=CartDTO()
            cart = request.session['cart']
            cart.addMaketa(maketaId, materijal, cijena, 1)
            request.session['cart']=cart
        return HttpResponseNotModified()