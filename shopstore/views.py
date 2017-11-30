from django.shortcuts import render, redirect
from shopstore import models, forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cart.cart import Cart 

# Create your views here.


def index(request, cat_id=0):

	all_categories = models.Category.objects.all()

	cart = Cart(request)

	all_products = None
	if int(cat_id) > 0:
		try:
			category = models.Category.objects.get(id=cat_id)
		except:
			category = None

		if category is not None:
			all_products = models.Product.objects.filter(category=category)

	if all_products is None:
		all_products = models.Product.objects.all()


	#--above code is created newest--
	
	#all_products = models.Product.objects.all()
	paginator = Paginator(all_products, 4)
	p = request.GET.get('p',1)
	try:
		products = paginator.page(p)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	return render(request,'index.html',locals())
	


def product(request, product_id):

	try:
		product = models.Product.objects.get(id=product_id)
	except:
		product = None

	return render(request,'product.html',locals())


def add_to_cart(request, product_id,quantity):
	product = models.Product.objects.get(id=product_id)
	cart = Cart(request)
	cart.add(product, product.price, quantity)
	return redirect('/')

def remove_from_cart(request, product_id):
	product= models.Product.objects.get(id=product_id)
	cart = Cart(request)
	cart.remove(product)
	return redirect('/cart/')

def cart(request):
	all_categories = models.Category.objects.all()
	cart = Cart(request)

	return render(request,'cart.html',locals())



def order(request):
	all_categories = models.Category.objects.all()
	cart = Cart(request)

	if request.method == 'POST':
		#user = User.objects.get(username=request.user.username)
		new_order = models.Order()

		form = forms.OrderForm(request.POST, instance=new_order)
		if form.is_valid():
			order = form.save()
			#email_messages = "您的购物内容如下：\n"
			for item in cart:
				models.OrderItem.objects.create(order=order,
												product=item.product,
												price=item.product.price,
												quantity=item.quantity)
				
			cart.clear()
			return redirect('/myorders/')
	else:
		form = forms.OrderForm()

	return render(request, 'order.html', locals())




def my_orders(request):
	all_categories = models.Category.objects.all()
	orders = models.Order.objects.all()

	return render(request,'myorders.html',locals())
