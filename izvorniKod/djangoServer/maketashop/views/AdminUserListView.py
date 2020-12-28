from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import render
from maketashop.DTOs.AULDTO import AULDTO
from maketashop.models import Korisnik

class AdminUserList(View):
    template_name ="maketashop/pregledKorisnika.html"

    def get(self, request):
        dto = AULDTO(request)

        if dto.getOvlast() == False:
            return HttpResponseRedirect(reverse('index'))
        
        return render(request, self.template_name, {
            'title': "pregledKorisnika", 
            'link_active': "pregledKorisnika", 
            'empty_head': False,
            'AdminUserListDTO' : dto,
            'session': request.session
            })

    def post(self, request):
        if (request.POST.get("pristup")):
            korisnikObj = Korisnik.objects.select_related().get(korisnikid=request.POST.get("id"))
            korisnikObj.dozvoljenpristup = not korisnikObj.dozvoljenpristup;
            korisnikObj.save()
                     
            return HttpResponseRedirect(self.request.path_info)

        elif (request.POST.get("search")):
            if request.POST.get("searchterm") == "":
                return HttpResponseRedirect(self.request.path_info)
            else:
                dto = AULDTO(request);
                dto.setSearchTerm(request.POST.get("searchterm"));
                return render(request, self.template_name, {
                    'title': "pregledKorisnika", 
                    'link_active': "pregledKorisnika", 
                    'empty_head': False,
                    'AdminUserListDTO' : dto,
                    'session': request.session
                    })
        elif (request.POST.get("userlink")):
            if request.POST.get("userlink") == "":
                return HttpResponseRedirect(self.request.path_info)
            else:
                s = "/maketashop/profilpregled/" + request.POST.get("userlink")
                return HttpResponseRedirect(s);
        else:
            print("U elseu")
            return HttpResponseRedirect(self.request.path_info)
            
