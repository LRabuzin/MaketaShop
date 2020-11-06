from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Cart(View):
    template_name ="cart.html"
    def get(self, request):
        # <view logic>
        
        return render(request, 'maketashop/cart.html', {
            'title': "cart", 
            'link_active': "cart", 
            'empty_head': False
            })