from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.TransakcijeDTO import TransakcijeDTO
from maketashop.models import Korisnik

class Transakcije(View):
    template_name ="maketashop/transakcije.html"
    def get(self, request):
        if (request.session.get("user")):
            dto = TransakcijeDTO();
            curr_user = Korisnik.objects.select_related().get(email=request.session.get("user"))
            if curr_user.jeadmin == True:
                TransakcijeDTO.setAdmin(dto);
            return render(request, self.template_name, {
            'title': "transakcije", 
            'link_active': "transakcije", 
            'empty_head': False,
            'TransakcijeDTO': dto,
            'session': request.session
            })
        else:
            return HttpResponseRedirect(reverse('index'))
            
    
