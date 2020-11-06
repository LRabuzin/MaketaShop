from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class B_Post(View):
    template_name ="maketashop/b_post.html"
    def get(self, request):
        # <view logic>
        
        return render(request, self.template_name, {
            'title': "b_post", 
            'link_active': "b_post", 
            'empty_head': False
            })