from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from maketashop.models import Prica
from maketashop.models import Napravljenaod
from maketashop.models import Komentar
from maketashop.models import Korisnik
from maketashop.DTOs.B_postDTO import B_postDTO
from django.urls import reverse

class B_Post(View):
    template_name ="maketashop/b_post.html"
    def get(self, request, id):
        
        #kod ako nije dozvoljen pristup korisniku
        if 'user' in request.session:
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))

        curr_user = None
        lajkao = 0
        if (request.session.get("user")):
            curr_user = Korisnik.objects.select_related().get(email=request.session.get("user"))
            if(curr_user.lajkaopricu.all().filter(pricaid=id)):
                lajkao = 1
            elif(curr_user.dislajkaopricu.all().filter(pricaid=id)):
                lajkao = -1

        
        return render(request, self.template_name, {
            'title': "Priča", 
            'link_active': "b_post", 
            'empty_head': False,
            'B_postDTO' : B_postDTO(id, lajkao),
            'user': curr_user,
            'session': request.session,
            })

    def post(self, request, id):
        korisnikObj = None
        if 'user' in request.session:
            korisnikObj = Korisnik.objects.select_related().get(email=request.session.get("user"))
            if not korisnikObj.dozvoljenpristup:
                return HttpResponseRedirect(reverse('logout'))
        #else:
        #    return HttpResponseRedirect(self.request.path_info)
        
        prica = Prica.objects.select_related().get(pricaid=id)

        if(request.POST.get("comment_text")):
            sadrzajK = request.POST.get("comment_text")
            obj = Komentar()
            obj.sadrzaj=sadrzajK
            obj.korisnikid=korisnikObj
            obj.pricaid=prica
            #obj = Komentar(sadrzaj=sadrzajK, korisnikid = korisnikObj, pricaid = prica)
            obj.save()

        # if (request.POST.get("userlink")):
        #     if request.POST.get("userlink") == "":
        #         return HttpResponseRedirect(self.request.path_info)
        #     else:
        #         s = "/maketashop/profilpregled/" + request.POST.get("userlink")
        #         return HttpResponseRedirect(s);

        if 'user' in request.session:
            if (request.POST.get("rate") == '1'):
                #print("U lajk postu sam");
                if (korisnikObj.lajkaopricu.all().filter(pricaid=id)):
                    #print("lajkao je vec");
                    obj = Prica.objects.select_related().get(pricaid=id)
                    obj.brojlajkova = obj.brojlajkova - 1
                    obj.save()
                    korisnikObj.lajkaopricu.remove(Prica.objects.select_related().get(pricaid=id))              
                else:
                    #print("nije lajkovao");
                    obj = Prica.objects.select_related().get(pricaid=id)
                    obj.brojlajkova = obj.brojlajkova + 1
                    korisnikObj.lajkaopricu.add(Prica.objects.select_related().get(pricaid=id))
                    if (korisnikObj.dislajkaopricu.all().filter(pricaid=id)):
                        korisnikObj.dislajkaopricu.remove(Prica.objects.select_related().get(pricaid=id))
                        obj.brojdislajkova = obj.brojdislajkova - 1
                    obj.save()
            elif (request.POST.get("rate") == '2'):
                if (korisnikObj.dislajkaopricu.all().filter(pricaid=id)):
                    #print("dislajkao vec")
                    obj = Prica.objects.select_related().get(pricaid=id)
                    obj.brojdislajkova = obj.brojdislajkova - 1
                    obj.save()
                    korisnikObj.dislajkaopricu.remove(Prica.objects.select_related().get(pricaid=id))
                else:
                    #print("nije dislajkao")
                    obj = Prica.objects.select_related().get(pricaid=id)
                    obj.brojdislajkova = obj.brojdislajkova + 1
                    korisnikObj.dislajkaopricu.add(Prica.objects.select_related().get(pricaid=id))
                    if (korisnikObj.lajkaopricu.all().filter(pricaid=id)):
                        korisnikObj.lajkaopricu.remove(Prica.objects.select_related().get(pricaid=id))
                        obj.brojlajkova = obj.brojlajkova - 1
                    obj.save()
        return HttpResponseRedirect(self.request.path_info)
