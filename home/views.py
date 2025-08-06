from django.shortcuts import render

from .models import Restaurant

# Create your views here.

def home_main(request):
    data = Restaurant.objects.first()

    context = {
        'rest_name':data.name
    }
    return render(request, 'home.html',context)