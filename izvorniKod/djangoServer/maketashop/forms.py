from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ime', 'class':'form-control my-input'}))
    surname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Prezime', 'class':'form-control my-input'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Korisničko ime', 'class':'form-control my-input'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class':'form-control my-input'}))
    pass1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Zaporka', 'class':'form-control my-input'}))
    pass2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Ponovljena zaporka', 'class':'form-control my-input'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Telefonski broj', 'class':'form-control my-input'}))
