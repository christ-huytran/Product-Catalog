from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'product/index.html')

def show(request, product_id):
	return render(request, 'product/show.html')