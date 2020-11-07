from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Cart(View):
    template_name ="maketashop/cart.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "cart", 
            'link_active': "cart", 
            'empty_head': False,
            'session': request.session
            })