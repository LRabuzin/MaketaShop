from django.urls import path
from maketashop.views.IndexView import Index
from maketashop.views.CartView import Cart
from maketashop.views.LoginView import Login
from maketashop.views.LogoutView import Logout
from maketashop.views.ProfilView import Profil
from maketashop.views.WebShopView import WebShop
from maketashop.views.B_PostView import B_Post
from . import views

#app_name ='maketashop'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cart/', Cart.as_view(), name='cart'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profil/', Profil.as_view(), name='profil'),
    # path('signup/', views.signup, name='signup'),
    path('webshop/', WebShop.as_view(), name='webshop'),
    path('post/', B_Post.as_view(), name='b_post'),
    # path('checkout/', views.checkout, name='checkout'),
    # path('maketa/', views.maketa, name='maketa'),
    # path('pregledKorisnika/', views.pregledKorisnika, name='pregledKorisnika'),
    # path('transakcije/', views.transakcije, name='transakcije'),
    # path('inbox/', views.inbox, name='inbox'),
    # path('interakcija/', views.interakcija, name='interakcija'),
]
