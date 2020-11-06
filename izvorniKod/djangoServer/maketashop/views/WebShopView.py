from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class WebShop(View):
    template_name ="WebShop.html"
    def get(self, request):
        # <view logic>
        
        return render(request, 'maketashop/WebShop.html', {
            'title': "webshop", 
            'link_active': "webshop", 
            'empty_head': False
            })