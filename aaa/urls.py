from django.urls import path
from . import views

urlpatterns= [    
    path('', views.articles, name="articles"),
    path('index/', views.index, name="index"),
    path('throw/', views.data_throw, name="data-throw"),
    path('catch/', views.data_catch, name="data-catch"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.article_detail, name="article_detail"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/update/', views.update, name="update"),
]