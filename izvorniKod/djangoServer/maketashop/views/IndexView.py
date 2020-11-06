from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Index(View):
    template_name ="maketashop/index.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "index", 
            'link_active': "index", 
            'empty_head': False
            })