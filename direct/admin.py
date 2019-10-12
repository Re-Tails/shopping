from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm, ProductCreationForm
from .models import User as CustomUser
from .models import Product, Transaction

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', ]

class ProductAdmin(admin.ModelAdmin):
    add_form = ProductCreationForm
    model = CustomUser
    list_display = ['name', 'price', 'stock', 'description', 'photo', 'category'
    , 'brand', 'rating', 'seller_fk', 'pubDate',]
    model = Product

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)
