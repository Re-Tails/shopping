from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=["firstName", "lastName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
#class RegistrationForm(forms.Form):
#    Name = forms.CharField()
#    Surname = forms.CharField()
