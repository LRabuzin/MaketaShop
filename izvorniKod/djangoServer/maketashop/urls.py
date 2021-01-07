from django.urls import path
from maketashop.views.IndexView import Index
from maketashop.views.CartView import Cart
from maketashop.views.LoginView import Login
from maketashop.views.LogoutView import Logout
from maketashop.views.ProfilView import Profil
from maketashop.views.ProfilPregledView import ProfilPregled
from maketashop.views.SignupView import Signup
from maketashop.views.WebShopView import WebShop
from maketashop.views.B_PostView import B_Post
from maketashop.views.CheckoutView import Checkout
from maketashop.views.MaketaView import Maketa
from maketashop.views.TransakcijeView import Transakcije
from maketashop.views.AdminUserListView import AdminUserList
from maketashop.views.InboxView import Inbox
from maketashop.views.InterakcijaTemaView import InterakcijaTema
from maketashop.views.InterakcijaMaketaView import InterakcijaMaketa
from maketashop.views.InterakcijaPricaView import InterakcijaPrica
from maketashop.views.SubmitionTemaView import SubmitionTema
from maketashop.views.SubmitionMaketaView import SubmitionMaketa
from maketashop.views.SubmitionPricaView import SubmitionPrica 
from maketashop.views.AdminMaketaView import AdminMaketa 
from maketashop.views.AdminMaterijalView import AdminMaterijal
from . import views

#app_name ='maketashop'
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('cart/', Cart.as_view(), name='cart'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profil/', Profil.as_view(), name='profil'),
    path('profilpregled/<int:id>/', ProfilPregled.as_view(), name='profilpregled'),
    path('signup/', Signup.as_view(), name='signup'),
    path('webshop/', WebShop.as_view(), name='webshop'),
    path('post/<int:id>/', B_Post.as_view(), name='b_post'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('maketa/<int:id>/', Maketa.as_view(), name='maketa'),
    path('pregledKorisnika/', AdminUserList.as_view(), name='pregledKorisnika'),
    path('transakcije/', Transakcije.as_view(), name='transakcije'),
    path('inbox/', Inbox.as_view(), name='inbox'),
    path('interakcijaTema/<int:id>/', InterakcijaTema.as_view(), name='interakcijaTema'),
    path('interakcijaMaketa/<int:id>/', InterakcijaMaketa.as_view(), name='interakcijaMaketa'),
    path('interakcijaPrica/<int:id>/', InterakcijaPrica.as_view(), name='interakcijaPrica'),
    path('temasubmit/', SubmitionTema.as_view(), name='temasubmit'),
    path('maketasubmit/', SubmitionMaketa.as_view(), name='maketasubmit'),
    path('postsubmit/', SubmitionPrica.as_view(), name='postsubmit'),
    path('adminmaketa/', AdminMaketa.as_view(), name='adminmaketa'),
    path('adminmaterijal/', AdminMaterijal.as_view(), name='adminmaterijal')
]
