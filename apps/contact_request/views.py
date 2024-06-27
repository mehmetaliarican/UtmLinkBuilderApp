# contact_request/views.py
from django.shortcuts import render, redirect
from .forms import ContactRequestForm
from django.http import Http404, HttpResponse
from django.conf import settings
from django.db import transaction
from django.apps import apps
from django.template import loader
import os

def contact_request_create(request):
    form_submitted = False
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            form_submitted = True
    else:
        form = ContactRequestForm()
    return render(request, 'contact_request/contact_us.html', {
        'form': form,
        'form_submitted': form_submitted
    })


def download_database(request):
    expected_key = 'TqEeAm6WJv2TO7NZQnTyHRVEetYla59G'  # Set your expected key here
    provided_key = request.GET.get('key', '')

    if provided_key != expected_key:
        return HttpResponse(status=403)  # Forbidden if the key doesn't match

    database_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    if os.path.exists(database_path):
        with open(database_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.sqlite3")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(database_path)
            return response
    raise Http404



def clear_custom_tables(request):
    expected_key = 'TqEeAm6WJv2TO7NZQnTyHRVEetYla59G'  # Set your expected key here
    provided_key = request.GET.get('key', '')

    if provided_key != expected_key:
        return HttpResponse(status=403)  # Forbidden if the key doesn't match

    # List of admin models to exclude
    admin_models = [
        'django_admin_log', 'auth_group', 'auth_group_permissions', 
        'auth_user', 'auth_user_groups', 'auth_user_user_permissions', 
        'django_content_type', 'django_migrations', 'django_session'
    ]

    with transaction.atomic():
        for model in apps.get_models():
            model_name = model._meta.db_table
            if model_name not in admin_models:
                model.objects.all().delete()

    context = {
        'status': 'success',
        'message': 'Custom tables cleared successfully'
    }
    return render(request, 'contact_request/cleared.html', context)