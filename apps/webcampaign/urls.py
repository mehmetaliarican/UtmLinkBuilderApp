from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('url/create/', views.web_campaign_url_create, name='create-web-campaign-url'),
]


admin.site.site_header = "Url Builder Admin"
admin.site.site_title = "Url Builder Portal"
admin.site.index_title = "Welcome to Admin Portal"