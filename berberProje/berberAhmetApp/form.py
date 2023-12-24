from django import forms
from .models import *
from django.contrib.auth.hashers import make_password

class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Şifre"
    )
    class Meta:
        model = AppUser
        fields = ["username","first_name", "last_name", "password", "tel" ]
        help_texts = {
            "username" : None
           
        }
        labels = {
            'username': "Kullanıcı Adı",
            "first_name":"İsim",
            "last_name":"Soyisim",
            'password': "Şifre",
        }
class RandevuForm(forms.ModelForm):

    class Meta:
        model = Randevu
        fields = [ "hizmet", "description" ]
        
class TatilForm(forms.ModelForm):

    class Meta:
        model = Tatil
        fields = [ "tatil" ]        
        widgets = {
            'tatil': forms.DateInput(attrs={'type': 'date'})
        }
   
class haftaTatilForm(forms.ModelForm):

    class Meta:
        model = haftaTatil
        fields = [ "gün" ]        
        
        

class UpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) 
    
    class Meta:
        model = AppUser
        fields = ["username","first_name", "last_name", "password", "tel" ]
        help_texts = {
            "username" : None
           
        }
        labels = {
            'username': "Kullanıcı Adı",
            'password': "Şifre"
        }        
    def save(self, commit=True):
        instance = super(UpdateForm, self).save(commit=False)
        password = self.cleaned_data.get('password')
        instance.set_password(password)  # Şifreyi ayarla
        if commit:
            instance.save()
        return instance