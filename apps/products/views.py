from django.shortcuts import render, redirect
from models import Product
# Create your views here.

def index(request):
	context = {
		'products' : Product.productManager.get()
	}
	return render(request, 'products/index.html', context)


def new(request):
	return render(request, 'products/create.html')

def create(request):
	if request.method == "POST":
		product_tuple = Product.productManager.create(request.POST['name'],request.POST['description'],request.POST['price'])
		if product_tuple[0] == False:
			print product_tuple[1].values()
			context = {
				'errors' : product_tuple[1].values()
			}
			return render(request, 'products/create.html', context)
		else:
			return redirect('/')
		
	return redirect('/')


def product(request, product_id):
	context = {
		'product' : Product.productManager.getProd(product_id)
	}
	return render(request, 'products/show.html', context)

def update(request, product_id):
	if request.method == "POST":
		product_tuple = Product.productManager.updateProd(product_id, request.POST['name'], request.POST['description'], request.POST['price'])
		if product_tuple[0] == False:
			print product_tuple[1].values()
			context = {
				'errors' : product_tuple[1].values()
			}
			return redirect('/edit/'+ product_id)
	return redirect('/')


def edit(request, product_id):
	context = {
		'product' : Product.productManager.getProd(product_id)
	}
	return render(request, 'products/edit.html', context)

def remove(request, product_id):
	Product.productManager.remove(product_id)
	return redirect('/')
