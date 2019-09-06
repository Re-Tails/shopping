from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer, Seller
from .models import User as CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["firstName", "lastName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"firstName":"First Name", "lastName":"Last Name", "email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class SellerCreationForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = ["sellerName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"sellerName": "Seller Name", "email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ["firstName", "lastName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"firstName":"First Name", "lastName":"Last Name", "email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class SellerChangeForm(UserChangeForm):
    class Meta:
        model = Seller
        fields = ["sellerName", "email", "password", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"sellerName": "Seller Name", "email":"Email", "password":"Password", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}
