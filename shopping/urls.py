from django.contrib import admin
from django.urls import path
from direct import views as direct_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('registerCustomer', direct_views.registerCustomer, name='registerCustomer'),
    path('registerSeller', direct_views.registerSeller, name='registerSeller'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile', direct_views.profile, name='profile'),
    path('addProduct/', direct_views.addProduct, name='add-product'),
    path('viewProduct/<int:id>', direct_views.viewProduct, name='view-product'),
    path('paymentPage/<int:id>', direct_views.paymentPage, name='payment-page'),
    path('', direct_views.index, name='index'),
    path('seller/<str:sellerName>', direct_views.seller, name='sellerPage'),
    path('viewTransaction/', direct_views.viewTransaction, name='view-transaction'),
    path('delete/<int:id>', direct_views.deleteProduct, name='deleteProduct')
    #path('profile/<int:id>', direct_views.sellerPage, name='seller-page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
