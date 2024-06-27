from django.urls import path
from . import views


app_name = 'webcampaign'
urlpatterns = [
    path('url/create/', views.web_campaign_url_create, name='create-web-campaign-url'),
]


