from django.urls import path
from . import views

urlpatterns= [    
    path('hello/', views.hello, name="hello"),
    path('throw/', views.data_throw, name="data-throw"),
    path('catch/', views.data_catch, name="data-catch"),
]