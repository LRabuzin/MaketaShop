from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica

class B_Post(View):
    template_name ="maketashop/b_post.html"
    def get(self, request, id):
        # <view logic>
        prica = Prica.objects.get(pricaid=id)
        return render(request, self.template_name, {
            'title': "b_post", 
            'link_active': "b_post", 
            'empty_head': False,
            'baza_data': prica
            })