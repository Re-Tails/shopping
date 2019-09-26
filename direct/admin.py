from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User as CustomUser
from .models import Product

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', ]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'description', 'photo', 'category'
    , 'brand', 'rating', 'seller', 'pubDate',]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product, ProductAdmin)
