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
            'form' : form,
            'session': request.session
            })
      else:
         return HttpResponseRedirect(reverse('index'))
   
   def post(self, request):
      form = LoginForm(request.POST)
      if form.is_valid():
         mail = form.cleaned_data['email']
         password = form.cleaned_data['pass1']
         if self.model_class.objects.filter(email=mail).exists():
            m = self.model_class.objects.get(email=mail)
            if m.lozinka == password:
               request.session['user'] = m.email
               request.session['admin'] = m.jeadmin
            return HttpResponseRedirect(reverse('index'))
      return HttpResponseRedirect(reverse('login'))
   
