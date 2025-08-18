from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('add-item',views.add_menu_item,name = 'add_item'),
    path('add-item-post',views.add_menu_item_post,name='add-item-post')
]