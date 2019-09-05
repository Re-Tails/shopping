from django import forms
from .models import Customer

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=["firstName", "lastName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels={"firstName":"First Name", "lastName":"Surname", "email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}
