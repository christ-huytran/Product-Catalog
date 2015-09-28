from django.shortcuts import render
from apps.product.models import Product, Manufacturer
# Create your views here.
def index(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	return render(request, 'product/index.html', context)

def show(request, product_id):
	return render(request, 'product/show.html')