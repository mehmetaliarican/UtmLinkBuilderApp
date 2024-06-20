from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index-page-default'),
    path('index', views.home, name='index-page'),
]
