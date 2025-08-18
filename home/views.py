from django.shortcuts import render,redirect
from datetime import datetime
from .models import Restaurant
from django.http import HttpResponse

from .froms import FeedbackForm

import logging

# Create your views here.

def home_main(request):
    data = Restaurant.objects.first()

    context = {
        'rest_name':data.name,
        'phone':data.phone,
        'address':data.address
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


def contact_us_post(request):
    name1 = request.POST['name']
    email1 = request.POST['email']
    message1 = request.POST['message']

    obj = contact()
    obj.name = name1
    obj.email = email1
    obj.message = message1
    obj.save()

    return HttpResponse("<script>alert('details submitted successfully');window.location='/'</script>")



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



def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('feedback_thankyou')

        else:
            from = FeedbackForm()
    return render(request, 'feedback.html',{'form':form})