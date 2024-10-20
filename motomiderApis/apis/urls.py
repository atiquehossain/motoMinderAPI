from django.urls import path

from . import views

urlpatterns = [
    path('', views.HelloApi.as_view(), name='motominder-v1'), 
]