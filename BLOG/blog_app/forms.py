from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import blog_posts

class sign_up_form(UserCreationForm):
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(label='FirstName',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(label='LastName',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class login_form(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('password'),strip=False,widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))

        
class post_form(forms.ModelForm):
    class Meta:
        model=blog_posts
        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TimeInput(attrs={'class':'form-control'}),
                        'desc':forms.Textarea(attrs={'class':'form-control'})}
