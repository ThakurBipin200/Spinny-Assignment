from django.urls import path
from store.views import (
    AddBoxView,
    ListAllBoxView,
    MyListBoxView,
    UpdateBoxView,
    DeleteBoxView
)

urlpatterns = [
    path('box/add/', AddBoxView.as_view(), name='add-box'),
    path('box/list_all_box/', ListAllBoxView.as_view(), name='list-all-box'),
    path('box/my_list/', MyListBoxView.as_view(), name='list-my-box'),
    path('box/update/<str:pk>/', UpdateBoxView.as_view(), name='update-box'),
    path('box/delete/<str:pk>/', DeleteBoxView.as_view(), name='delete-box')
]
