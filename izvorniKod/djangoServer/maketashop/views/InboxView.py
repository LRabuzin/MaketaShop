from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View

class Inbox(View):
    template_name ="maketashop/inbox.html"
    def get(self, request):
        
        return render(request, self.template_name, {
            'title': "inbox", 
            'link_active': "inbox", 
            'empty_head': False
            })