from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class PregledKorisnika(View):
    template_name ="maketashop/pregledKorisnika.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "pregledKorisnika", 
            'link_active': "pregledKorisnika", 
            'empty_head': False
            })