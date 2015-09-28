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
	return render(request, 'product/show.html')

def create(request):
	manufacturer = Manufacturer.objects.get(id = request.POST['manufacturer'])
	new_product = Product(manufacturer = manufacturer, product_name = request.POST['product_name'], price = request.POST['price'], description = request.POST['description'])
	new_product.save()
	return redirect('index')