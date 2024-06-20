# contact_request/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_request_create, name='create_contact_request'),
    path('download-db/', views.download_database, name='download_database'),
]
