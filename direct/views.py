from django.shortcuts import render, redirect
from direct.forms import CustomerCreationForm, SellerCreationForm, ProductCreationForm, CardCreationForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from direct.models import Seller, Product, Customer, Transaction, Card

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

def viewProduct(request, id):
    data = Product.objects.all().filter(pk=id)
    context={
        'data': data
    }
    return render(request, 'viewProduct.html', context)

@login_required
def paymentPage(request, id):
    if request.user.isSeller:
        return redirect('login')
    #added
    if request.method == "POST":
        form = CardCreationForm(request.POST)
        if form.is_valid():
            try:
                temp = Card.objects.get(number=form.cleaned_data.get('number'))
            except Card.DoesNotExist:
                tempForm = form.save()
                tempTrans = Transaction()
                tempTrans.total = Product.objects.get(id=id).price
                tempTrans.product = Product.objects.get(id=id)
                tempTrans.customer = Customer.objects.get(pk=request.user.pk)
                tempTrans.card = tempForm
                tempTrans.save()
                #update redirect to a confirmation page
                return redirect('login')
            else:
                #update redirect to a confirmation page
                tempTrans = Transaction()
                tempTrans.total = Product.objects.get(id=id).price
                tempTrans.product = Product.objects.get(id=id)
                tempTrans.customer = Customer.objects.get(pk=request.user.pk)
                tempTrans.card = temp
                tempTrans.save()
                return redirect('profile')
    else:
        form = CardCreationForm()
    #end added
    product = Product.objects.all().filter(pk=id)
    print(product)

    customer = Customer.objects.all().filter(pk=request.user.pk)
    print(customer)
    context={
        'products': product,
        'customers': customer,
        'form': form
    }
    return render(request, 'paymentForm.html', context)

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

@login_required
def viewTransaction(request):
    if request.user.isSeller:
        return redirect('login')
    else:
        products = []
        list = []
        transactions = Transaction.objects.all().filter(customer_id = request.user.pk)
        customers = Customer.objects.all().filter(pk = request.user.pk)
        for transaction in transactions:
            products.append(Product.objects.get(pk = transaction.product_id))

        zip_data = zip(products, transactions, customers)
        context = {
            'transactions': transactions,
            'customers': customers,
            'products': products,
            'zip_data': zip_data
        }
    return render(request, 'viewTransaction.html', context)
