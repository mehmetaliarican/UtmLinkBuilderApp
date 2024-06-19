from django.shortcuts import render

# utm_parameters/views.py
from django.shortcuts import render, redirect
from .models import WebCampaignUrl
from .forms import CreateWebCampaignUrlForm

def web_campaign_url_create(request):
    if request.method == "POST":
        form = CreateWebCampaignUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_url_created')
    else:
        form = CreateWebCampaignUrlForm()
    return render(request, 'webcampaign/create_url.html', {'form': form})
