from django.contrib import admin

from .models import SEOSettings

# Register your models here.
class SEOSettingsAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'title')
    search_fields = ('app_name', 'title')
    
    def has_add_permission(self, request):
        # Allow adding if there's no existing instance for the app
        app_name = request.GET.get('app_name')
        if app_name:
            return not SEOSettings.objects.filter(app_name=app_name).exists()
        return True

admin.site.register(SEOSettings, SEOSettingsAdmin)