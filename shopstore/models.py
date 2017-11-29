from django.db import models
from filer.fields.image import FilerImageField
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200);

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	sku = models.CharField(max_length=20)
	name = models.CharField(max_length=200)
	description = models.TextField()
	image = FilerImageField(related_name='product_image')
	website = models.URLField(null=True)
	stock = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=10,decimal_places=2,default=0)

	def __str__(self):
		return self.name


class Order(models.Model):
	user = models.CharField(max_length=50)
	full_name = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	phone = models.CharField(max_length=11)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return 'Order:{}'.format(self.id)


class OrderItem(models.Model):
	order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return '{}'.format(self.id)
