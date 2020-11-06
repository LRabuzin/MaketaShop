from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class Maketa(View):
    template_name ="maketashop/maketa.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "maketa", 
            'link_active': "maketa", 
            'empty_head': False
            })