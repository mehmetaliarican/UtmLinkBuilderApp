# homepage/middleware.py
from django.urls import resolve
from .models import SEOSettings  # Ensure the import path is correct

class SEOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_app = resolve(request.path_info).app_name

        try:
            seo = SEOSettings.objects.get(app_name=current_app)
        except SEOSettings.DoesNotExist:
            seo = None
        request.seo_title = seo.title if seo else ''
        request.seo_description = seo.description if seo else ''
        request.seo_keywords = seo.keywords if seo else ''

        response = self.get_response(request)
        return response
