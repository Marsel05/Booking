from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import *


class CustomSignupForm(SignupForm):
    country = forms.CharField(max_length=100, label=_('Country'))
    phone_number = forms.IntegerField(label=_('Phone Number'))
    postal_code = forms.IntegerField(label=_('Postal Code'))
    city = forms.CharField(max_length=100, label=_('City'))
    address = forms.CharField(max_length=100, label=_('address'))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']

        if phone_number < 0:
            raise ValidationError(_('Phone number should be a positive number'))

        return phone_number

    def save(self, request):
        user = super().save(request)

        country = self.cleaned_data['country']
        phone_number = self.cleaned_data['phone_number']
        city = self.cleaned_data['city']
        postal_code = self.cleaned_data['postal_code']
        address = self.cleaned_data['address']

        user.userprofile.country = country
        user.userprofile.city = city
        user.userprofile.postal_code = postal_code
        user.userprofile.address = address
        user.userprofile.phone_number = phone_number
        user.userprofile.save()

        return user



