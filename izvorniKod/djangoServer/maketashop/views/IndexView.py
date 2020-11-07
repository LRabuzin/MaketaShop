from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica

class Index(View):
    template_name ="maketashop/index.html"
    def get(self, request):
        price = Prica.objects.all().select_related()
        return render(request, self.template_name, {
            'title': "index", 
            'link_active': "index", 
            'empty_head': False,
            'baza_data': price,
            'session': request.session
            })
