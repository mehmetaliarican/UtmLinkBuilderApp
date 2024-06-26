from django.contrib import admin
from .models import  WebCampaignUrl


class WebCampaignUrlsAdmin(admin.ModelAdmin):
    list_display = ('website_url','utm_source', 'utm_medium', 'utm_term', 'utm_content',)
    search_fields = ('website_url','utm_source', 'utm_medium',  'utm_term', 'utm_content')
    
    def has_add_permission(self, request):
        return False  # Disable the add feature
    
    def has_delete_permission(self, request):
        return False  # Disable the delete feature

admin.site.register(WebCampaignUrl, WebCampaignUrlsAdmin)