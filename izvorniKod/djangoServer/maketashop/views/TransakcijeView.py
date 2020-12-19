from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.TransakcijeDTO import TransakcijeDTO

class Transakcije(View):
    template_name ="maketashop/transakcije.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "transakcije", 
            'link_active': "transakcije", 
            'empty_head': False,
            'TransakcijeDTO': TransakcijeDTO(),
            'session': request.session
            })
    
