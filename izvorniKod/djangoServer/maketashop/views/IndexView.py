from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class Index(TemplateView):
    template_name ="index.html"
    def get(self, request):
        # <view logic>
        
        return render(request, 'maketashop/index.html', {
            'title': "index", 
            'link_active': "index", 
            'empty_head': False
            })