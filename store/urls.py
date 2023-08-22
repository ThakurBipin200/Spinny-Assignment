from django.urls import path
from rest_framework.authtoken import views
from store.views import *


urlpatterns = [

    path('box/add/',add_box,name='add-box'),
    path('box/list_all_box/',list_all_box,name='list-all-box'),
    path('box/my_list/',my_list_box,name='list-my-box'),
    path('box/update/<str:pk>',update_box,name='update-box'),
    path('box/delete/<str:pk>',delete_box,name='delete-box')

]
