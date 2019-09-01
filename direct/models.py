from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=32)
    isSeller = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=15)
    street = models.CharField(max_length=50)
    suburb = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    joinedDate = models.DateField()

    def __str__(self):
        return self.email

class Customer(User):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)


class Seller(User):
    sellerName = models.CharField(max_length=30)

    def __str__(self):
        return self.sellerName

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField(default="No description provided")
    photo = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    rating = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    pubDate = models.DateField(name='date publised')

    def __str__(self):
        return self.name

class Card(models.Model):
    number = models.IntegerField(max_length=20)
    name = models.CharField(max_length=60)
    expiryDate = models.DateField()
    cvv = models.IntegerField(max_length=4)

    def __str__(self):
        return self.number
