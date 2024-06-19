from django.shortcuts import render, redirect
from .forms import CreatePlayCampaignUrlForm

def play_campaign_url_create(request):
    if request.method == 'POST':
        form = CreatePlayCampaignUrlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campaign_url_created')  # Redirect to a success page or desired URL
    else:
        form = CreatePlayCampaignUrlForm()
    
    return render(request, 'playcampaign/create_url.html', {'form': form})
