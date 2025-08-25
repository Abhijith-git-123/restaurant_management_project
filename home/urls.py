from django.urls import path
from .views import *

urlpatterns = [

    path('/',views.base, name='base'),
    path('login',views.login, name = 'login'),
    path('home',views.home_main,name = 'home'),
    path('about',views.about_page, name = 'about'),
    path('404',views.404_not found, name = '404'),
    path('contact_us',views.contact_us,name="contact_us"),
    path('contact_us_post',views.contact_us_post,name="contact_us_post"),
    path('reservation',views.reservation,name = "reservation"),
    path('feedback',views.feedback, name = 'feedback')

    
]