from django.shortcuts import render

from .models import Restaurant

# Create your views here.

def home_main(request):
    data = Restaurant.objects.first()

    context = {
        'rest_name':data.name
        'phone':data.phone
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