from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.CartDTO import CartDTO
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

class Cart(View):
    template_name ="maketashop/cart.html"
    def get(self, request):
        if 'cart' in request.session:
            Cart=request.session['cart']
        else:
            Cart=CartDTO()
        return render(request, self.template_name, {
            'title': "cart", 
            'link_active': "cart", 
            'empty_head': False,
            'cartDTO' : Cart,
            'session': request.session
            })

    def post(self, request):
        if 'metoda' in request.POST:
                if 'cart' in request.session:
                    cart = request.session['cart']
                    
                    if request.POST['metoda'] == '1':
                        cart.removeSveOdMaketa(maketaId, materijal, cijena)
                    
                    #dodavanje jednog itema
                    elif request.POST['metoda'] == '2':
                        cart.addMaketa(maketaId, materijal, cijena, 1)
                    
                    #micanje jednog itema
                    elif request.POST['metoda'] == '3':
                        cart.addMaketa(maketaId, materijal, cijena, 1)
                    
                    request.session['cart'] = cart
        return HttpResponseRedirect(self.request.path_info)