from django.db import models
from .models import OrderStatus

# Create your models here.
class Order(models.Model):
    status=models.ForeignKey('OrderStatus',on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return f"Order #{self.id}-{self.status}"

from orders.models import Order,OrderStatus
status=OrderStatus.objects.create(name="Pending")
order=Order.objects.create(status=status)
print(order.status)