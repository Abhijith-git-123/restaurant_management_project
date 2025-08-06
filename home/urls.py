from django.urls import path
from .views import *

urlpatterns = [

    path('',views.home_main,name = 'home'),
    path('about',views.about_page, name = 'about')
    path('404',views.404_not found, name = '404')

    
]