from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.AULDTO import AULDTO

class AdminUserList(View):
    template_name ="maketashop/pregledKorisnika.html"

    def get(self, request):
        
        return render(request, self.template_name, {
            'title': "pregledKorisnika", 
            'link_active': "pregledKorisnika", 
            'empty_head': False,
            'AdminUserListDTO' : AULDTO(request),
            'session': request.session
            })
