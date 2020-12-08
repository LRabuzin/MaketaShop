from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.WebShopDTO import WebShopDTO

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