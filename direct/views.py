from django.shortcuts import render, redirect
from direct.forms import CustomerCreationForm, SellerCreationForm, ProductCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from direct.models import Seller

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
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} just created a seller account.')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid information entered')
    else:
        form = CustomerCreationForm()
    context = {
        'title': "Register",
        'form': form}
    return render(request, 'register.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')

def addProduct(request):
    if not request.user.is_authenticated:
        return redirect('login')
    for seller in Seller.objects.all():
        if seller.pk != request.user.pk:
            return redirect('login')
    if request.method == "POST":
        form = ProductCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.warning(request, 'Invalid information enterred')
    else:
        form = ProductCreationForm()
    context = {
        'form': form
    }
    return render(request, 'addProduct.html', context)
