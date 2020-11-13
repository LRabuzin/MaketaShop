from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse

class Logout(View):
    template_name ="logout"
    def get(self, request):
      if 'user' in request.session:
         del request.session['user']
         return HttpResponseRedirect(reverse('index'))
      else:
         return HttpResponseRedirect(reverse('login'))