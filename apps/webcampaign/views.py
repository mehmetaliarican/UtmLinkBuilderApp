from django.shortcuts import render, redirect
from urllib.parse import urlencode
from .models import WebCampaignUrl
from .forms import CreateWebCampaignUrlForm

def web_campaign_url_create(request):
    url_created = False
    generated_url = ''
    if request.method == "POST":
        form = CreateWebCampaignUrlForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            url_created = True
            base_url = campaign.website_url
            utm_params = {
                'utm_source': campaign.utm_source,
                'utm_medium': campaign.utm_medium,
                'utm_campaign': campaign.utm_campaign,
                'utm_id': campaign.utm_id,
                'utm_term': campaign.utm_term,
                'utm_content': campaign.utm_content,
            }
            generated_url = f"{base_url}?{urlencode(utm_params)}"
    else:
        form = CreateWebCampaignUrlForm()
    return render(request, 'webcampaign/create_url.html', {
        'form': form,
        'url_created': url_created,
        'generated_url': generated_url
    })
