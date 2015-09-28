from django.shortcuts import render, redirect
from apps.product.models import Product, Manufacturer
# Create your views here.
def index(request):
	products = Product.objects.all()
	manufacturers = Manufacturer.objects.all()
	context = {
		'products': products,
		'manufacturers': manufacturers
	}
	return render(request, 'product/index.html', context)

def show(request, product_id):
	product = Product.objects.get(id = product_id)
	manufacturers = Manufacturer.objects.all()
	context = {
		'product': product,
		'manufacturers': manufacturers
	}
	return render(request, 'product/show.html', context)

def create(request):
	manufacturer = Manufacturer.objects.get(id = request.POST['manufacturer'])
	new_product = Product(manufacturer = manufacturer, product_name = request.POST['product_name'], price = request.POST['price'], description = request.POST['description'])
	new_product.save()
	return redirect('index')

def update(request, product_id):
	product = Product.objects.get(id = product_id)
	product.product_name = request.POST['product_name']
	product.price = request.POST['price']
	product.description = request.POST['description']
	product.manufacturer = Manufacturer.objects.get(id = request.POST['manufacturer'])
	product.save()
	return redirect('index')