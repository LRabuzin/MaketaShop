from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica
from maketashop.models import Napravljenaod
from maketashop.models import Komentar

class B_Post(View):
    template_name ="maketashop/b_post.html"
    def get(self, request, id):
        # <view logic>
        prica = Prica.objects.select_related().get(pricaid=id)
        napod = Napravljenaod.objects.get(maketaid=prica.maketaid)
        koment = Komentar.objects.filter(pricaid=prica.pricaid)
        
        return render(request, self.template_name, {
            'title': "b_post", 
            'link_active': "b_post", 
            'empty_head': False,
            'baza_data': prica,
            'baza_data_2': napod,
            'baza_data_3': koment,
            'session': request.session
            })

    def post(self, request, id):
        if(request.POST.get("koment")):
            print(request.POST.get("koment"))
        if (request.POST.get("rate") == '1'):
            obj = Prica.objects.select_related().get(pricaid=id)
            obj.brojlajkova = obj.brojlajkova + 1
            obj.save()
        elif (request.POST.get("rate") == '2'):
            obj = Prica.objects.select_related().get(pricaid=id)
            obj.brojdislajkova = obj.brojdislajkova + 1
            obj.save()
        return HttpResponseRedirect(self.request.path_info)
