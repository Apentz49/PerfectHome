from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from homes.models import Home


class CustomerCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class HomeSearchForm(forms.Form):
    search = forms.CharField(max_length=50)
    zipcode = forms.CharField(max_length=50)
    bedrooms = forms.CharField(max_length=20)
    bathrooms = forms.CharField(max_length=30)
    min_price = forms.CharField(max_length=20)
    max_price = forms.CharField(max_length=20)

    class Meta:
        model = Home
        fields = ('zipcode', 'bedrooms', 'bathrooms', 'min_price', 'max_price')