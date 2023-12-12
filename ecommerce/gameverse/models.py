from django.db import models
from django.contrib.auth.models import User

class Catogery(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ["name"]
    def __str__(self): 
        return self.name
    
class Product(models.Model):
    catogery = models.ManyToManyField(Catogery)
    id = models.IntegerField(primary_key=True,default=1)
    name = models.CharField(max_length=350)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="static/uploads/")
    
    class Meta:
        ordering = ["name"]
    def __str__(self):
        return f"product id {self.id} and name is {self.name}"
    
class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self): 
        return f"{self.quantity} X {self.product.name} Price {self.product.price}"

    def calculate_total_per_item(self):
        total = self.product.price * self.quantity
        return total

    def save(self, *args, **kwargs):
        self.p_per_item = self.calculate_total_per_item()
        super().save(*args, **kwargs)
    
    
    
    



