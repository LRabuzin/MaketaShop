from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class Transakcije(View):
    template_name ="maketashop/transakcija.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "transakcije", 
            'link_active': "transakcije", 
            'empty_head': False,
            'session': request.session
            })