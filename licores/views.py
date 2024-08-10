from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from licores.forms import CustomerForm, CategoryForm, ProductForm, SaleForm
from .models import Customer, Category, Product, Sale

class CustomLoginView(LoginView):
    template_name = 'login.html'

def index(request):
    return render(request, 'index.html')

def customer(request):
    customers = Customer.objects.order_by('last_name')
    template = loader.get_template('customer.html')
    return HttpResponse(template.render({'customers': customers}, request))

def info_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk= customer_id)
    template = loader.get_template('display_customer.html')
    context = {
        'customer': customer
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licores:customer')
    else:
        form = CustomerForm()   
    return render(request, 'customer_form.html', {'form': form})

@login_required
def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk = id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('licores:customer')
    else:
        form = CustomerForm(instance=customer)       
    return render(request, 'customer_form.html', {'form': form})

@login_required
def delete_customer(request, id):
    customer = get_object_or_404(Customer, pk = id)
    customer.delete()
    return redirect("licores:customer")



def category(request):
    categorys = Category.objects.order_by('name')
    template = loader.get_template('category.html')
    return HttpResponse(template.render({'categorys': categorys}, request))

def info_category(request, category_id):
    category = get_object_or_404(Category, pk= category_id)
    template = loader.get_template('display_category.html')
    context = {
        'category': category
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licores:category')
    else:
        form = CategoryForm()   
    return render(request, 'category_form.html', {'form': form})

@login_required
def edit_category(request, id):
    category = get_object_or_404(Category, pk = id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('licores:category')
    else:
        form = CategoryForm(instance=category)       
    return render(request, 'category_form.html', {'form': form})

@login_required
def delete_category(request, id):
    category = get_object_or_404(Category, pk = id)
    category.delete()
    return redirect("licores:category")



def product(request):
    products = Product.objects.order_by('name')
    template = loader.get_template('product.html')
    return HttpResponse(template.render({'products': products}, request))

def info_product(request, product_id):
    product = get_object_or_404(Product, pk= product_id)
    template = loader.get_template('display_product.html')
    context = {
        'product': product
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licores:product')
    else:
        form = ProductForm()   
    return render(request, 'product_form.html', {'form': form})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk = id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('licores:product')
    else:
        form = ProductForm(instance=product)       
    return render(request, 'product_form.html', {'form': form})

@login_required
def delete_product(request, id):
    product = get_object_or_404(Product, pk = id)
    product.delete()
    return redirect("licores:product")



def sale(request):
    sales = Sale.objects.order_by('product')
    template = loader.get_template('sale.html')
    return HttpResponse(template.render({'sales': sales}, request))

def info_sale(request, sale_id):
    sale = get_object_or_404(Sale, pk= sale_id)
    template = loader.get_template('display_sale.html')
    context = {
        'sale': sale
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licores:sale')
    else:
        form = SaleForm()   
    return render(request, 'sale_form.html', {'form': form})


@login_required
def edit_sale(request, id):
    sale = get_object_or_404(Sale, pk = id)
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('licores:sale')
    else:
        form = SaleForm(instance=sale)       
    return render(request, 'sale_form.html', {'form': form})

@login_required
def delete_sale(request, id):
    sale = get_object_or_404(Sale, pk = id)
    sale.delete()
    return redirect("licores:sale")