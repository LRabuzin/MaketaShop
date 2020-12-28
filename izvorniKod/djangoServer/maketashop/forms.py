from django import forms
from django.core import validators

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
    pic = forms.BooleanField(label="Prikaži sliku", required=False)
    name_surname = forms.BooleanField(label="Prikaži prezime", required=False)
    birth_date = forms.BooleanField(label="Prikaži rođendan", required=False)
    register_date = forms.BooleanField(label="Prikaži datum registracije", required=False)
    email = forms.BooleanField(label="Prikaži adresu e-pošte", required=False)
    address = forms.BooleanField(label="Prikaži adresu", required=False)

class PostForm(forms.Form):
    naslovprice = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov priče', 'class':'form-control my-input', 'id':'naslovprice'}))
    text1 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput1', 'readonly':'True'}))
    media1 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])], widget = forms.ClearableFileInput(attrs={'id':'mediaInput1', 'readonly':'True'}))
    text2 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput2', 'readonly':'True'}))
    media2 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])], widget = forms.ClearableFileInput(attrs={'id':'mediaInput2', 'readonly':'True'}))
    text3= forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput3', 'readonly':'True'}))
    media3 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])], widget = forms.ClearableFileInput(attrs={'id':'mediaInput3', 'readonly':'True'}))
    text4 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput4', 'readonly':'True'}))
    media4 = forms.FileField(required=False, validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])], widget = forms.ClearableFileInput(attrs={'id':'mediaInput4', 'readonly':'True'}))
    text5 = forms.CharField(required=False, widget = forms.Textarea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input', 'id':'textInput5', 'readonly':'True'}))
    
class InteractionThemeForm(forms.Form):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))
    ime_teme = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov priče', 'class':'form-control my-input'}))
    tekst_teme = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Sadržaj teme', 'class':'form-control my-input'}))

class MaketaForm(forms.Form):
    ime_makete = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime makete', 'class':'form-control my-input'}))
    dimenzije = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Dimenzije', 'class':'form-control my-input'}))
    opis = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Opis', 'class':'form-control my-input'}))

class InteractionPostForm(PostForm):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))

class AdminPostForm(PostForm, MaketaForm):
    includes_maketa = forms.BooleanField(label="Uključuje maketu", required=False, widget=forms.CheckboxInput(attrs={'id':'includesMaketa'}))
    unique_cijena = forms.DecimalField(label="Cijena:", min_value = 0, decimal_places = 2)
    broj_na_skladistu = forms.IntegerField(label="Broj na skladištu:", min_value = 0)
    osnovna_slika = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png'])])

class InteractionMaketaForm(MaketaForm):
    naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))

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
    # paypal_bool = forms.BooleanField(label=)
    broj_kartice = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Broj kartice', 'class':'form-control my-input'}))
    istek_kartice = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY', 'class':'form-control my-input'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV', 'class':'form-control my-input'}))