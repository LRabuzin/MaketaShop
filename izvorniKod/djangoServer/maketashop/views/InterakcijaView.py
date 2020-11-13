from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class Interakcija(View):
    template_name ="maketashop/interakcija.html"
    def get(self, request):

        return render(request, self.template_name, {
            'title': "interakcija", 
            'link_active': "interakcija", 
            'empty_head': False,
            'session': request.session
            })