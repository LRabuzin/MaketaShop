from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class B_Post(View):
    template_name ="b_post.html"
    def get(self, request):
        # <view logic>
        
        return render(request, 'maketashop/b_post.html', {
            'title': "b_post", 
            'link_active': "b_post", 
            'empty_head': False
            })