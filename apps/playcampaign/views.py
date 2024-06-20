from django.shortcuts import render, redirect
from urllib.parse import urlencode
from .models import PlayCampaignUrl
from .forms import CreatePlayCampaignUrlForm

def play_campaign_url_create(request):
    url_created = False
    generated_url = ''
    if request.method == 'POST':
        form = CreatePlayCampaignUrlForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            url_created = True
            base_url = "https://play.google.com/store/apps/details"
            referrer_params = {
                'utm_source': campaign.campaign_source,
                'utm_medium': campaign.campaign_medium,
                'utm_term': campaign.campaign_term,
                'utm_content': campaign.campaign_content,
                'utm_campaign': campaign.campaign_name,
                'anid': campaign.ad_network,
            }
            referrer = urlencode(referrer_params)
            generated_url = f"{base_url}?id={campaign.application_id}&referrer={referrer}"
    else:
        form = CreatePlayCampaignUrlForm()
    
    return render(request, 'playcampaign/create_url.html', {
        'form': form,
        'url_created': url_created,
        'generated_url': generated_url
    })
