from django.shortcuts import render, redirect
from direct.forms import CustomerCreationForm, SellerCreationForm
from django.views.generic import TemplateView


def registerCustomer(request):
    if request.method == "POST":
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin')
        #For now after the user hits submit, they will be redirected to the admin page.
        #We should make some sort of confirmation page, or maybe redirect them to the login page.
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
            return redirect('admin')
        #For now after the user hits submit, they will be redirected to the admin page.
        #We should make some sort of confirmation page, or maybe redirect them to the login page.
    form = SellerCreationForm()
    context = {
        'title': "Register",
        'form': form}
    return render(request, 'register.html', context)
