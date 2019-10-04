from django.shortcuts import render, redirect
from direct.forms import CustomerCreationForm, SellerCreationForm, ProductCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from direct.models import Seller, Product

def index(request):
    return render(request, 'index.html')

def registerCustomer(request):
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} just created a customer account.')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid information entered')
    else:
        form = CustomerCreationForm()
    context = {
        'title': "Register",
        'form': form}
    return render(request, 'register.html', context)

def registerSeller(request):
    if request.method == "POST":
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form = form.save(commit=False)
            form.isSeller = True
            form.save()
            messages.success(request, f'{username} just created a seller account.')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid information entered')
    else:
        form = SellerCreationForm()
    context = {
        'title': "Register",
        'form': form}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def addProduct(request):
    if request.user.isSeller:
        pass
    else:
        return redirect('login')
    if request.method == "POST":
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.seller_id = request.user.pk
            temp = temp.save()
            return redirect('login')
        else:
            messages.warning(request, 'Invalid information enterred')
    else:
        form = ProductCreationForm()
    context = {
        'form': form
    }
    return render(request, 'addProduct.html', context)

def index(request):
    products = Product.objects.all()
    context = {
        'title' : 'Home',
        'products' : products
    }
    return render(request, 'index.html', context)

def seller(request, sellerName):
    seller = Seller.objects.get(sellerName = sellerName).user_ptr_id
    products = Product.objects.all().filter(seller = seller)
    context = {
        'title' : 'Home',
        'products' : products
    }
    return render(request, 'index.html', context)