from django.contrib import admin
from .models import PlayCampaignUrl

class PlayCampaignUrlAdmin(admin.ModelAdmin):
    list_display = ['ad_network', 'application_id', 'campaign_source', 'campaign_name']
    
    def has_add_permission(self, request):
        # Disable add permission
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Disable delete permission
        return False

admin.site.register(PlayCampaignUrl, PlayCampaignUrlAdmin)
