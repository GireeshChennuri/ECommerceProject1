from django.db import models
from user.models import *
from products.models import *
import uuid
   
class Order(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING='pending'
        CONFIRMED='confirmed'
        CANCELLED='cancelled'
    order_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=10,choices=StatusChoices.choices,default=StatusChoices.PENDING)
    products=models.ManyToManyField(Product,through="OrderItem",related_name="orders")
    
    def __str__(self):
        return f"Order {self.order_id} created by {self.user.username}"
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()

    @property
    def item_subtotal(self):
        return self.product.price*self.quantity

    def __str__(self):
        return f"{self.quantity}x{self.product.name} in order {self.order.order_id}"
     
