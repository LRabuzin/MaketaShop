from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
        if maketaId in request.POST:
            maketaID = request.POST['maketaId']
            cijena = request.POST['cijena']
            materijal = request.POST['materijal']

            if not 'cart' in request.session:
                request.session['cart']=CartDTO()
            request.session['cart'].addMaketa(maketaID, cijena, materijal, 1)
        else:
             return HttpResponseRedirect(reverse('webshop'))