# contact_request/urls.py
from django.urls import path
from . import views

app_name = 'contact_request'

urlpatterns = [
    path('', views.contact_request_create, name='create_contact_request'),
    path('download-db/', views.download_database, name='download_database'),
    path('clear_custom_tables/', views.clear_custom_tables, name='clear_custom_tables'),
]
