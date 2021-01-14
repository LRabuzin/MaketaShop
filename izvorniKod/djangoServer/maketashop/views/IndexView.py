from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica
from maketashop.DTOs.IndexDTO import IndexDTO
from maketashop.models import Korisnik
from django.urls import reverse

class Index(View):
    template_name ="maketashop/index.html"
    def get(self, request):

        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))
        return render(request, self.template_name, {
            'title': "Početna", 
            'link_active': "index", 
            'empty_head': False,
            'IndexDTO': IndexDTO(),
            'session': request.session
            })
