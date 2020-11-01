from django.urls import path

from . import views

#app_name ='maketashop'
urlpatterns = [
    path('', views.index, name='index'),
    #path('index/', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('profil/', views.profil, name='profil'),
    path('signup/', views.signup, name='signup'),
    path('webshop/', views.webshop, name='webshop'),
    path('post/', views.b_post, name='b_post'),
    path('checkout/', views.checkout, name='checkout'),
    path('maketa/', views.maketa, name='maketa'),
    path('pregledKorisnika/', views.pregledKorisnika, name='pregledKorisnika'),
    path('transakcije/', views.transakcije, name='transakcije'),
    path('inbox/', views.inbox, name='inbox'),
    path('interakcija/', views.interakcija, name='interakcija'),
]
