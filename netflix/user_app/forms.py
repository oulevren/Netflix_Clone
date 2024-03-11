from django import forms
from netflix_app.models import *

class UserForm(forms.ModelForm):

    email = forms.CharField(label="",widget=forms.EmailInput(attrs={'placeholder':'E-mail Adresi'}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder':'Şifre'}))

    class Meta:
        model = NetflixUser
        fields = ["email","username","password"]

        # help_texts = {
        #     'username': None,
        #     'password': None
        # }

        # #widget ekledikten sonra email sil
        # labels = {
        #     'password': "",
        #     'username': "",
        #     'email': ""
        # }