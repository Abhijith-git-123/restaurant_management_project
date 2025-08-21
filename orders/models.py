from django.db import models

from django.contrib.auth.models import User
from products.models import Item

from products.import MenuItem


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


@api_view(['GET'])
def get_menu(request):
    menu = [
        {
            "name":"chichen pizza",
            "description":"classic pizza with tomato sauce, and chicke",
            "price":299
        },

        {
            "name":"veggie Burger",
            "description":"Loaded veggie patty with lettuce, tomato, and cheese",
            "price":199
        },
        {
            "name":"Pasta Allfredo",
            "description":"Creamy pasta with mushroom and permesan cheese",
            "price":247
        }
    ]
    return Response(menu)



class Cart(models.Model):
    user = models.Foreignkey(User, on_delete=models.CASCADE)
    item = models.Foreignkey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.user.username} - {self.item.name} ({self.quantity})"