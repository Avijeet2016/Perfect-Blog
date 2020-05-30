from django import forms
from django.contrib.auth.models import User 
from .models import Profile, Contact, About


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'
        