from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.MaketaDTO import MaketaDTO
from maketashop.DTOs.CartDTO import CartDTO
from maketashop.models import Napravljenaod
from maketashop.models import Materijal, Korisnik


class Maketa(View):
    template_name ="maketashop/maketa.html"
    def get(self, request, id):
        #kod ako nije dozvoljen pristup korisniku
        if Korisnik.objects.filter(email=request.session['user']).exists():
            if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                return HttpResponseRedirect(reverse('logout'))

        return render(request, self.template_name, {
            'title': "maketa", 
            'link_active': "maketa", 
            'empty_head': False,
            'maketaDTO':MaketaDTO(id),
            'session': request.session
            })

    def post(self, request, id):
        if 'cijena' in request.POST:
            maketaId = int(id)
            materijal = request.POST['materijal']
            #cijena = float(request.POST['cijena'])
            cijena = float(Napravljenaod.objects.get(materijalid=Materijal.objects.get(ime=materijal), maketaid=maketaId).cijena)
            

            if not 'cart' in request.session:
                request.session['cart']=CartDTO()
            cart = request.session['cart']
            cart.addMaketa(maketaId, materijal, cijena, 1)
            request.session['cart']=cart
        return HttpResponseRedirect(self.request.path_info)