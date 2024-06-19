# contact_request/views.py
from django.shortcuts import render, redirect
from .forms import ContactRequestForm

def contact_request_create(request):
    if request.method == "POST":
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_request_created')
    else:
        form = ContactRequestForm()
    return render(request, 'contact_request/contact_us.html', {'form': form})
