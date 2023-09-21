from django.urls import path
from django.urls import re_path
from .import views

urlpatterns = [
    path('', views.index),
    re_path(r'^about', views.about),
    re_path(r'^content', views.content),
    path('products/<int:product_id>', views.products),
    path('products/', views.products),
    path('users/<int:id>/<name>', views.users),
    path('users/', views.users),
    path('details/', views.details),
    path('access/<int:age>', views.access),
]
