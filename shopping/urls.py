"""shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from direct import views as direct_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('registerCustomer/', direct_views.registerCustomer, name='registerCustomer'),
    path('registerSeller/', direct_views.registerSeller, name='registerSeller'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', direct_views.profile, name='profile'),
    path('addProduct/', direct_views.addProduct, name='add-product'),
    path('viewProduct/<int:id>', direct_views.viewProduct, name='view-product'),
    path('paymentPage/<int:id>', direct_views.paymentPage, name='payment-page'),
    path('', direct_views.index, name='index'),
    path('seller/<str:sellerName>', direct_views.seller, name='sellerPage'),
    path('viewTransaction/', direct_views.viewTransaction, name='view-transaction'),
    #path('profile/<int:id>', direct_views.sellerPage, name='seller-page'),
]
