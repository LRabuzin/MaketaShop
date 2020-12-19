from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.CartDTO import CartDTO

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
            'cart' : Cart,
            'session': request.session
            })