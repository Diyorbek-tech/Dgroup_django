from django import forms

class homeform(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.PasswordInput()
    email=forms.EmailField()
