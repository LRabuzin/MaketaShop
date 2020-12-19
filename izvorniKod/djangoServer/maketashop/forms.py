from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime', 'class':'form-control my-input'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prezime', 'class':'form-control my-input'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Korisničko ime', 'class':'form-control my-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class':'form-control my-input'}))
    pass1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Zaporka', 'class':'form-control my-input'}))
    pass2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Ponovljena zaporka', 'class':'form-control my-input'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Telefonski broj', 'class':'form-control my-input'}))

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

# class BlogPostForm(forms.Form):
#     naslovprice = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov priče', 'class':'form-control my-input'}))
#     text1 = forms.CharField(widget = forms.TextArea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input'}))
#     media1 = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])])
#     text2 = forms.CharField(widget = forms.TextArea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input'}))
#     media2 = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])])
#     text3= forms.CharField(widget = forms.TextArea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input'}))
#     media3 = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])])
#     text4 = forms.CharField(widget = forms.TextArea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input'}))
#     media4 = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png', 'mkv', 'avi', 'mov', 'mp4'])])
#     text5 = forms.CharField(widget = forms.TextArea(attrs={'placeholder': 'Tekst priče', 'class':'form-control my-input'}))
    
# class InteractionThemeForm(forms.Form):
#     naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))
#     ime_teme = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov priče', 'class':'form-control my-input'}))
#     tekst_teme = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Sadržaj teme', 'class':'form-control my-input'}))

# class MaketaForm(forms.Form):
#     ime_makete = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime makete', 'class':'form-control my-input'}))
#     dimenzije = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Ime makete', 'class':'form-control my-input'}))
#     opis = forms.CharField(max_length=160, widget=forms.TextInput(attrs={'placeholder': 'Ime makete', 'class':'form-control my-input'}))

# class InteractionBlogPostForm(BlogPostForm):
#     naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))

# class AdminBlogPostForm(BlogPostForm, MaketaForm):
#     includes_maketa = forms.BooleanField(label="Uključuje maketu", required=False)

# class InteractionMaketaForm(MaketaForm):
#     naslov_interakcije = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Naslov interakcije', 'class':'form-control my-input'}))

# class AdminMaketaForm(MaketaForm):
#     osnovna_slika = forms.FileField(validators = [validators.FileExtensionValidator(['jpg', 'jpeg', 'gif', 'png'])])
#     broj_na_skladistu = forms.IntegerField(min_value = 0)
#     drvo_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)
#     plastika_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)
#     aluminij_cijena = forms.DecimalField(min_value = 0, decimal_places = 2)