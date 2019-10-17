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
    products = []
    if request.user.isSeller:
        currentUser = Seller.objects.get(pk=request.user.pk)
        products = Product.objects.all().filter(seller_fk = request.user.pk)
    else:
        currentUser = Customer.objects.get(pk=request.user.pk)
    context = {
        'currentUser': currentUser,
        'products': products
    }
    return render(request, 'profile.html', context)

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
            temp.seller_fk_id = request.user.pk
            temp = temp.save()
            return redirect('index')
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
    context = {
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
                print(id)
                tempTrans.total = Product.objects.get(id=id).price
                tempTrans.product_fk = Product.objects.get(id=id)
                tempTrans.customer_fk = Customer.objects.get(pk=request.user.pk)
                tempTrans.card_fk = tempForm
                print(tempTrans.total)
                tempTrans.save()
                #update redirect to a confirmation page
                return redirect('login')
            else:
                #update redirect to a confirmation page
                tempTrans = Transaction()
                tempTrans.total = Product.objects.get(id=id).price
                tempTrans.product_fk = Product.objects.get(id=id)
                tempTrans.customer_fk = Customer.objects.get(pk=request.user.pk)
                tempTrans.card_fk = temp
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
    seller = Seller.objects.get(sellerName = sellerName)
    products = Product.objects.all().filter(seller_fk = seller.id)
    context = {
        'title' : 'Home',
        'seller' : seller,
        'products' : products
    }
    return render(request, 'sellerPublic.html', context)

@login_required
def viewTransaction(request):
    if request.user.isSeller:
        allProducts = Product.objects.all().filter(seller_fk = request.user.pk)
        allTransactions = Transaction.objects.all()
        customers = []
        products = []
        transactions = []
        for transaction in allTransactions:
            for product in allProducts:
                if transaction.product_fk_id == product.pk:
                    transactions.append(transaction)
                    products.append(product)
                    customers.append(Customer.objects.get(pk=transaction.customer_fk_id))

        zipdata = zip(transactions, products, customers)

        context = {
            'transactions': transactions,
            'customers': customers,
            'products': products,
            'zipdata': zipdata
        }
        return render(request, 'viewTransactionSeller.html', context)
    else:
        products = []
        list = []
        transactions = Transaction.objects.all().filter(customer_fk = request.user.pk)
        customers = Customer.objects.all().filter(pk = request.user.pk)
        for transaction in transactions:
            products.append(Product.objects.get(pk = transaction.product_fk_id))
        context = {
            'transactions': transactions,
            'customers': customers,
            'products': products,
        }
        return render(request, 'viewTransaction.html', context)

@login_required
def deleteProduct(request, id):
    product = Product.objects.get(id = id)
    if (request.user.id == product.seller_fk_id):
        context = {
            'title': "Delete Listing",
            'product': product
        }
        product.delete()
        return redirect('index')
    else:
        return redirect('index')
