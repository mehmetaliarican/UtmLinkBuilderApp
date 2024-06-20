from django.db import models
from django.utils import timezone


class WebCampaignUrl(models.Model):
    website_url = models.CharField(max_length=100)  # Required
    utm_id = models.CharField(max_length=100, blank=True, null=True)  # Optional
    utm_source = models.CharField(max_length=100)  # Required
    utm_medium = models.CharField(max_length=100)  # Required
    utm_campaign = models.CharField(max_length=100, blank=True, null=True)  # Optional
    utm_term = models.CharField(max_length=100, blank=True, null=True)  # Optional
    utm_content = models.CharField(max_length=100, blank=True, null=True)  # Optional
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Web Campaign Url"
        verbose_name_plural = "Web Campaign Urls"

    def __str__(self) -> str:
        return f"WebCampaignUrl for {self.contact_request}"
