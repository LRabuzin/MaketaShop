from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica
from maketashop.DTOs.IndexDTO import IndexDTO

class Index(View):
    template_name ="maketashop/index.html"
    def get(self, request):
        return render(request, self.template_name, {
            'title': "index", 
            'link_active': "index", 
            'empty_head': False,
            'IndexDTO': IndexDTO(),
            'session': request.session
            })
