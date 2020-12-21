from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from maketashop.DTOs.MaketaDTO import MaketaDTO
from maketashop.DTOs.CartDTO import CartDTO

class Maketa(View):
    template_name ="maketashop/maketa.html"
    def get(self, request, id):

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
            cijena = float(request.POST['cijena'])
            materijal = request.POST['materijal']

            if not 'cart' in request.session:
                request.session['cart']=CartDTO()
            cart = request.session['cart']
            cart.addMaketa(maketaId, materijal, cijena, 1)
            request.session['cart']=cart
        return HttpResponseRedirect(self.request.path_info)