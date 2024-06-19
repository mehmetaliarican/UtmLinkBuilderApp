# contact_request/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.contact_request_create, name='create_contact_request'),
]
