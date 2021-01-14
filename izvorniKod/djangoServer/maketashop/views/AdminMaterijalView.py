from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from ..forms import MaterijalForm


from maketashop.models import Materijal
from maketashop.models import Korisnik

from django.contrib import messages



class AdminMaterijal(View):
   template_name ="maketashop/adminMaterijal.html"

   def get(self, request):
      # <view logic>
      form = MaterijalForm()
      if 'user' not in request.session:
         messages.add_message(request, messages.ERROR, 'Potreban je login.')
         return HttpResponseRedirect(reverse('login'))
      else:
         user = Korisnik.objects.select_related().get(email = request.session['user'])
         if not user.jeadmin:
            messages.add_message(request, messages.ERROR, 'Nemate dovoljnu razinu ovlasti.')
            return HttpResponseRedirect(reverse('index'))
         return render(request, self.template_name, {
         'title': "Dodaj materijal", 
         'link_active': "adminMaterijal", 
         'empty_head': False,
         'form' : form,
         'session': request.session
         })

   def post(self, request):
      form = MaterijalForm(request.POST)
      if form.is_valid():

         materijal = Materijal()
         materijal.ime = form.cleaned_data['custom_materijal']
         materijal.save()
         messages.add_message(request, messages.SUCCESS, 'Dodan novi materijal.')
         return HttpResponseRedirect(reverse('index'))

      messages.add_message(request, messages.ERROR, 'Svi uvjeti nisu zadovoljeni.')
      return HttpResponseRedirect(reverse('index'))