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