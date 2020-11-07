from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from maketashop.models import Korisnik
from ..forms import LoginForm

class Login(View):
   model_class = Korisnik
   template_name ="maketashop/login.html"
   
   def get(self, request):
      form = LoginForm()
      if 'user' not in request.session:
         return render(request, self.template_name, {
            'title': "login", 
            'link_active': "login", 
            'empty_head': False,
            'form' : form
            })
      else:
         return HttpResponseRedirect(reverse('index'))
   
   def post(self, request):
      if self.model_class.objects.filter(email=request.POST.get('exampleInputEmail1')).exists():
         mail = request.POST.get('exampleInputEmail1')
         password = request.POST.get('exampleInputPassword1')
         m = self.model_class.objects.get(email=request.POST.get('exampleInputEmail1'))
         if m.lozinka == password:
            request.session['user'] = m.email
            return HttpResponseRedirect(reverse('index'))
         else:
            return HttpResponseRedirect(reverse('index'))
      else:
         return HttpResponseRedirect(reverse('login'))
   