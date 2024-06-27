# homepage/context_processors.py
def seo_settings(request):
    return {
        'seo_title': getattr(request, 'seo_title', ''),
        'seo_description': getattr(request, 'seo_description', ''),
        'seo_keywords': getattr(request, 'seo_keywords', ''),
    }
