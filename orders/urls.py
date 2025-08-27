from django.urls import path
from .views import *

urlpatterns = [
    path('order/confirmation', views.order_confirmation, name='order_confirmation')
]