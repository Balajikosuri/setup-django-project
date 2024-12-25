from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.hello_world, name='hello_world'),
    
]

