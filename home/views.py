from django.shortcuts import render,redirect
from datetime import datetime
from .models import Restaurant
from django.http import HttpResponse

from .froms import FeedbackForm,ContactForm

from orders.models import Cart

import logging

# Create your views here.





def home_main(request):
    data = Restaurant.objects.first()
    menu_items = MenuItem.objects.all()[:6]

    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user = request.user).count()

    context = {
        'rest_name':data.name,
        'phone':data.phone,
        "email":data.email,
        'address':data.address,
        'current_year':datetime.now().year,
        'menu_items':menu_items,
        'opening_hours':data.opening_hours,
        'cart_count':cart_count,
        'current_datetime':datetime.now(),

       
    }
    return render(request, 'home.html',context)



def about_page(request):

    data = Restaurant.objects.all()

    context = {
        'rest_name':data.name,
        'history':data.history,
        'mission':data.mission,
        'logo':data.logo,
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

    form = ContactForm()
    return render(request, 'contact.html',contact, {'form':form})


def contact_us_post(request):
    # name1 = request.POST['name']
    # email1 = request.POST['email']
    # message1 = request.POST['message']

    # obj = contact()
    # obj.name = name1
    # obj.email = email1
    # obj.message = message1
    # obj.save()

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()



    #send Email Notification to restaurnt

            subject = f"New Contact Message from {name1}"

            message = f""" You receive a new message from your website:

            Name: {name1}
            Email: {email1}
            Message: {message1}

            """
            restaurnt_email = "myrestaurant@gmail.com"

            send_mail(
                subject,
                message,
                'myrestaurant@gmail.com',
                [restaurnt_email],
                fail_silently = False,
            )

        


            return HttpResponse("<script>alert('details submitted successfully');window.location='/'</script>")

        else:
            return render(request, 'contact.html', {'form':form})



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


def faq(request):
    faq = [
        {"question":"What are Your opening hour?", "answer": "we are open Mon-Fri: 11am-9pm, Sat-Sun: 10am - 10pm"},
        {"question":"Do you offer home delivery?", "answer": "Yes, we provide home delivary within a 5km radious."},
        {"question":"Can I book a table online?", "answer": "Currently, we only accept walk-in customers, but online booking is coming soon!"},
        {"question":"Do you have vegitarian options?", "answer": "Absolutely! we have a wide range of vegitarian and vegan dishes."},
    ] 

    return render(request, "faq.html", {"faqs": faqs})