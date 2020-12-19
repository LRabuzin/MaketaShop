from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.MaketaDTO import MaketaDTO

class Maketa(View):
    template_name ="maketashop/maketa.html"
    def get(self, request, id):

        return render(request, self.template_name, {
            'title': "maketa", 
            'link_active': "maketa", 
            'empty_head': False,
            'maketaDTO':MaketaDTO(id),
            'session': request.session
            })

    def post(self, request):
        return HttpResponseRedirect(self.request.path_info)