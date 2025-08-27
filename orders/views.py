from django.shortcuts import render

# Create your views here.

import random
from django.shortcuts import render

def order_confirmation(request):
  

    order_number = random.randint(1000, 9999)

    context = {
        "rest_name":"Thiruvonam Retaurant",
        "order_number": order_number

    }
    return render(request, "order_confirmation.html",context)
