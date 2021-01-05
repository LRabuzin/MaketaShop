from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from datetime import datetime
from maketashop.DTOs.InboxDTO import InboxDTO
from maketashop.models import Korisnik

class Inbox(View):
    template_name ="maketashop/inbox.html"


    def get(self, request):
        
        if 'user' not in request.session:
            return HttpResponseRedirect(reverse('login'))
        else:
            user = Korisnik.objects.select_related().get(email = request.session['user'])
            
            #kod ako nije dozvoljen pristup korisniku
            if Korisnik.objects.filter(email=request.session['user']).exists():
                if not Korisnik.objects.get(email=request.session['user']).dozvoljenpristup:
                    return HttpResponseRedirect(reverse('logout'))

            return render(request, self.template_name, {
            'title': "inbox", 
            'link_active': "inbox", 
            'empty_head': False,
            'InboxDTO' : InboxDTO(request.session['user']),
            'jeAdmin' : user.jeadmin,
            'session': request.session
            })