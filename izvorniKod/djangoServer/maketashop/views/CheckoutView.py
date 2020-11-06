from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class Checkout(View):
    template_name ="maketashop/checkout.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "checkout", 
            'link_active': "checkout", 
            'empty_head': False
            })