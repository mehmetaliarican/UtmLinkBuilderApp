from django.contrib import admin
from django.contrib.auth.models import Group
from .models import ContactRequest
from django.utils.html import format_html

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email_link', 'mobile', 'companyWebSite', 'created', 'isHandled')
    list_filter = ('isHandled',)  # Add filter for isHandled
    search_fields = ('name', 'surname', 'email', 'mobile', 'companyWebSite')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(isHandled=False)  # Filter to show only not handled requests

    def has_add_permission(self, request):
        return False  # Disable the add feature
    
    def has_delete_permission(self, request,obj=None):
        return False  # Disable the delete feature

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['name', 'surname', 'email', 'mobile', 'companyWebSite', 'created']
        return []

    fields = ['name', 'surname', 'email', 'mobile', 'companyWebSite', 'created', 'isHandled']

    def email_link(self, obj):
        return format_html('<a href="https://calendly.com/{}" target="_blank">{}</a>', obj.email, obj.email)
    email_link.short_description = 'Email'



admin.site.unregister(Group)

admin.site.register(ContactRequest, ContactRequestAdmin)