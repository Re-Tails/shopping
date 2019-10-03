from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length = 32, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=32)
    isSeller = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=15)
    street = models.CharField(max_length=50)
    suburb = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    joinedDate = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.email

class Customer(User):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30, blank=True, null=True)

class Seller(User):
    sellerName = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    rating = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    pubDate = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.name

class Card(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    expiryDate = models.DateField()
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return self.number

class Transaction(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    paidTime = models.DateTimeField(default=datetime.datetime.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)