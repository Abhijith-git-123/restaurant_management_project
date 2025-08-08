from django.shortcuts import render
from datetime import datetime
from .models import Restaurant

import logging

# Create your views here.

def home_main(request):
    data = Restaurant.objects.first()

    context = {
        'rest_name':data.name,
        'phone':data.phone,
        'current_year':datetime.now().year
    }
    return render(request, 'home.html',context)



def about_page(request):

    data = Restaurant.objects.all()

    context = {
        'rest_name':data.name
    }

    return render(request, 'about.html',context)


def 404_not_found(request):
    return render(request, '404.html')


def contact_us(request):

    data = Restaurant.objects.all()

    contect = {
        'rest:name':data.aname,
        'phone':data.phone,
        'email':data.email
    }
    return render(request, 'contact.html')


logger = logging.getLogger(__name__)

def list_menu(request):

    try:
        menu_items = [
            {'name':'Chicken Biriyani', 'Price':250},
            {'name': 'Paneer Butter Masala', 'Price': 180},
            {'name': 'Veg Biriyani', 'Price': 220},
            {'name': 'chicken Tikka', 'Price': 300}
        ]

        context = {
            'rest_name': 'Thiruvonam Restaurant',
            'menu_items': menu_items,
        }
        return render(request,'menu.html',context)

    except Exception as e:
        logger.error("Error in menu_view: %s" e)
        return HttpResponseServerError("something went wrong.please try agian later")




def reservation(request):

    data = Restaurant.objects.all()

    context = {
        'phone':data.phone
    }
    return render(request, 'reservation.html',context)