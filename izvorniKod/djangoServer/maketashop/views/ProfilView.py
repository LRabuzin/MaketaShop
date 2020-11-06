from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Profil(View):
    template_name ="profil.html"
    def get(self, request):
        # <view logic>
        
        return render(request, 'maketashop/profil.html', {
            'title': "profil", 
            'link_active': "profil", 
            'empty_head': False
            })