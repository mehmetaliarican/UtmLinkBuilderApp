from django.urls import path
from . import views

urlpatterns = [
    path('url/create/', views.web_campaign_url_create, name='create-web-campaign-url'),
]
