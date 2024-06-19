from django.urls import path
from . import views

urlpatterns = [
    path('url/create/', views.play_campaign_url_create, name='create-play-campaign-url'),
]
