from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customer, Seller, Product, Card
from .models import User as CustomUser

class CardCreationForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ["number", "name", "expiryDate", "cvv"]

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model =  Product
        fields = ["name", "price", "stock", "description", "photo", "category", "brand", "rating"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ["username", "username", "firstName", "lastName", "email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"username":"Username", "firstName":"First Name", "lastName":"Last Name", "email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class SellerCreationForm(UserCreationForm):
    class Meta:
        model = Seller
        fields = ["username", "username", "sellerName", "email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"username":"Username", "sellerName": "Seller Name", "email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"username":"Username", "email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class CustomerChangeForm(UserChangeForm):
    class Meta:
        model = Customer
        fields = ["username", "firstName", "lastName", "email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"username":"Username", "firstName":"First Name", "lastName":"Last Name", "email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}

class SellerChangeForm(UserChangeForm):
    class Meta:
        model = Seller
        fields = ["username", "sellerName", "email", "phoneNumber", "street", "suburb", "postcode", "state", "country"]
        labels = {"username":"Username", "sellerName": "Seller Name", "email":"Email", "phoneNumber":"Phone Number", "street":"Street Name", "suburb":"Suburb", "postcode":"Postcode", "state":"State", "country":"Country"}
