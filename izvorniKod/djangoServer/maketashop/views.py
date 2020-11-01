from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'maketashop/index.html')

def cart(request):
    return render(request, 'maketashop/cart.html')

def login(request):
    return render(request, 'maketashop/login.html')

def profil(request):
    return render(request, 'maketashop/profil.html')

def signup(request):
    return render(request, 'maketashop/signup.html')

def webshop(request):
    return render(request, 'maketashop/WebShop.html')

def b_post(request):
    return render(request, 'maketashop/b_post.html')

def checkout(request):
    return render(request, 'maketashop/checkout.html')

