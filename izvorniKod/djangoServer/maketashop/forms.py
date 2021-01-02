from django import forms
from django.core import validators
from maketashop.models import Materijal
from django.core.exceptions import ValidationError

def file_size(value):
    limit = 500 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Datoteka prevelika, veličina ne smije prelaziti 500 MB')

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime', 'class':'form-control my-input'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prezime', 'class':'form-control my-input'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Korisničko ime', 'class':'form-control my-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class':'form-control my-input'}))
    pass1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Zaporka', 'class':'form-control my-input'}))
    pass2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Ponovljena zaporka', 'class':'form-control my-input'}))
    adress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Adresa', 'class':'form-control my-input'}))
    cardNumber = forms.CharField(max_length=21, widget=forms.TextInput(attrs={'placeholder': 'Broj kartice', 'class':'form-control my-input'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class':'form-control'}))
    pass1 = forms.CharField(label="Zaporka", max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Zaporka', 'class':'form-control'}))

class PrivacyForm(forms.Form):
    pic = forms.BooleanField(label="Sakrij sliku", required=False)
    name_surname = forms.BooleanField(label="Sakrij ime i prezime", required=False)
    birth_date = forms.BooleanField(label="Sakrij rođendan", required=False)
    register_date = forms.BooleanField(label="Sakrij datum registracije", required=False)
    email = forms.BooleanField(label="Sakrij adresu e-pošte", required=False)
    address = forms.BooleanField(label="Sakrij adresu", required=False)

class PostForm(forms.Form):
    naslovprice = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov priče', 'class':'form-control my-input', 'id':'naslovprice'}))
    text1 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput1', 'readonly':'True'}))
    media1 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4']), file_size], widget = forms.ClearableFileInput(attrs={'id':'mediaInput1', 'readonly':'True'}))
    text2 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput2', 'readonly':'True'}))
    media2 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4']), file_size], widget = forms.ClearableFileInput(attrs={'id':'mediaInput2', 'readonly':'True'}))
    text3= forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput3', 'readonly':'True'}))
    media3 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4']), file_size], widget = forms.ClearableFileInput(attrs={'id':'mediaInput3', 'readonly':'True'}))
    text4 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput4', 'readonly':'True'}))
    media4 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4']), file_size], widget = forms.ClearableFileInput(attrs={'id':'mediaInput4', 'readonly':'True'}))
    text5 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput5', 'readonly':'True'}))
    
class InteractionThemeForm(forms.Form):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))
    ime_teme = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov teme', 'class':'form-control my-input'}))
    tekst_teme = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Sadržaj teme', 'class':'form-control my-input'}))

class MaketaForm(forms.Form):
    ime_makete = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime makete', 'class':'form-control my-input'}))
    dimenzije = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Dimenzije', 'class':'form-control my-input'}))
    opis = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Opis', 'class':'form-control my-input'}))

class InteractionPostForm(PostForm):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))

class InteractionMaketaForm(MaketaForm):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))
    materijal = forms.ModelChoiceField(queryset=Materijal.objects.all().order_by('materijalid'), empty_label = None, widget=forms.Select(attrs={'class':'form-control my-input'}))

class AdminMaketaForm(MaketaForm):
    osnovna_slika = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png'])])
    broj_na_skladistu = forms.IntegerField(min_value = 0)
    drvo_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)
    plastika_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)
    aluminij_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)

class PlacanjeForm(forms.Form):
    ime = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Ime', 'class':'form-control my-input'}))
    prezime = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Prezime', 'class':'form-control my-input'}))
    adresa = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Adresa', 'class':'form-control my-input'}))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class':'form-control my-input'}))
    ime_na_kartici = forms.CharField(max_length=27, widget=forms.TextInput(attrs={'placeholder': 'Ime i prezime nositelja kartice', 'class':'form-control my-input'}))
    PAYMENTMETHODS = [
    ('kreditnaKartica', 'Kreditna kartica'),
    ('paypal', 'PayPal'),
    ]
    paypal_bool = forms.ChoiceField(label='Vrsta plaćanja', choices=PAYMENTMETHODS, widget=forms.RadioSelect)
    broj_kartice = forms.CharField(max_length=16, min_length=16, widget=forms.TextInput(attrs={'placeholder': 'Broj kartice', 'class':'form-control my-input'}))
    istek_kartice = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY', 'class':'form-control my-input'}))
    cvv = forms.CharField(max_length=3, min_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV', 'class':'form-control my-input'}))

class AdminCijenaForm(forms.Form):
    custom_cijena = forms.DecimalField(label="Cijena:", min_value = 0, decimal_places = 2)
