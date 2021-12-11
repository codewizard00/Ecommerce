from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to="product")
    product_price =models.IntegerField()
    product_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE )    
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    