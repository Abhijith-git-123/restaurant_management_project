from django.db import models

from django.contrib.auth.models import User
from products.models import Item


class order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('PROCESSING','Processing'),
        ('COMPLETED','Completed'),
        ('CANCELLED','Cancelled'),
    ]

    customer = models.Foreignkey(User, on_delete = models.CASCADE, related_name = 'orders')
    order_items = models.ManyToManyField(Menu, related_name = 'orders')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_status  = models.CharField(max_length = 20, choices = STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username} - {self.order_status}"


