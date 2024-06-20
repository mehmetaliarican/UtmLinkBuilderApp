# contact_request/views.py
from django.shortcuts import render, redirect
from .forms import ContactRequestForm
from django.http import Http404, HttpResponse
from django.conf import settings
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
    database_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    if os.path.exists(database_path):
        with open(database_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.sqlite3")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(database_path)
            return response
    raise Http404