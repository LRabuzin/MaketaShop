from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from maketashop.models import Korisnik
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'maketashop/index.html', {
        'title': "index", 
        'link_active': "index", 
        'empty_head': False
        })

def cart(request):
    return render(request, 'maketashop/cart.html', {
        'title': "cart", 
        'link_active': "cart", 
        'empty_head': False
        })

def logout(request):
    if 'user' in request.session:
        del request.session['user']
        request.session['empty_head'] = False
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))
def login(request):
    if 'user' not in request.session:
        if request.method == 'POST':

            if Korisnik.objects.filter(email=request.POST.get('exampleInputEmail1')).exists():
                mail = request.POST.get('exampleInputEmail1')
                password = request.POST.get('exampleInputPassword1')
                m = Korisnik.objects.get(email=request.POST.get('exampleInputEmail1'))
                if m.lozinka == password:
                    request.session['user'] = m.email
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'maketashop/login.html', {'title': "login", 'link_active': "login", 'empty_head': False})
    else:
       return HttpResponseRedirect(reverse('index'))

def profil(request):
    return render(request, 'maketashop/profil.html', {
        'title': "profil", 
        'link_active': "profil", 
        'empty_head': False
        })

def signup(request):
    if 'user' not in request.session:
        if request.method == 'POST':
            if Korisnik.objects.filter(email=request.POST.get('email')).exists():
                return HttpResponseRedirect(reverse('signup'))
            else:
                korisnik = Korisnik()
                korisnik.korisnickoime = request.POST.get('email')
                korisnik.email = request.POST.get('email')
                korisnik.lozinka = request.POST.get('pass1')
                korisnik.razinaautoriteta = 1
                korisnik.rodendan = "1999-10-15"
                korisnik.datumregistracije = "1999-10-15"
                korisnik.save()

                request.session['user'] = korisnik.email
                request.session['empty_head'] = True
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'maketashop/signup.html', {
                'title': "signup", 
                'link_active': "signup", 
                'empty_head': False
                })
    else:
        return HttpResponseRedirect(reverse('index'))

def webshop(request):
    return render(request, 'maketashop/WebShop.html', {
        'title': "webshop", 
        'link_active': "webshop", 
        'empty_head': False
        })

def b_post(request):
    return render(request, 'maketashop/b_post.html', {
        'title': "b_post", 
        'link_active': "b_post", 
        'empty_head': False
        })

def checkout(request):
    return render(request, 'maketashop/checkout.html', {
        'title': "checkout", 
        'link_active': "checkout", 
        'empty_head': False
        })

def maketa(request):
    return render(request, 'maketashop/maketa.html', {
        'title': "maketa", 
        'link_active': "maketa", 
        'empty_head': False
        })
    
def pregledKorisnika(request):
    return render(request, 'maketashop/pregledKorisnika.html', {
        'title': "pregledKorisnika", 
        'link_active': "pregledKorisnika", 
        'empty_head': False
        })

def transakcije(request):
    return render(request, 'maketashop/transakcije.html', {
        'title': "transakcije", 
        'link_active': "transakcije", 
        'empty_head': False
        })

def inbox(request):
    return render(request, 'maketashop/inbox.html', {
        'title': "inbox", 
        'link_active': "inbox", 
        'empty_head': False
        })

def interakcija(request):
    return render(request, 'maketashop/interakcija.html', {
        'title': "interakcija", 
        'link_active': "interakcija", 
        'empty_head': False
        })
