from django.db import models
from .models import OrderStatus

# Create your models here.
class Order(models.Model):
    name=models.CharField(max_length=50,unique=True)
    status=models.ForeignKey('OrderStatus',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"Order #{self.id}-{self.status}"

from orders.models import Order,OrderStatus
status=OrderStatus.objects.create(name="Pending")
order=Order.objects.create(status=status)
print(order.status)

class Coupon(models.Model):
    code=models.CharField(max_length=50,unique=True)
    discount_percentage=models.DecimalField(max_digits=5,decimal_places=2)
    is_active=models.BooleanField(default=True)
    valid_from=models.DateField()
    valid_until=models.DateField()

    def __str__(self):
        return f"{self.code}({self.discount_percentage}% off)"