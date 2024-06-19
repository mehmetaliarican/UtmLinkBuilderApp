from django.db import models

class PlayCampaignUrl(models.Model):
    ad_network = models.CharField(max_length=100)
    application_id = models.CharField(max_length=100)
    campaign_source = models.CharField(max_length=100)
    campaign_medium = models.CharField(max_length=100, blank=True, null=True)
    campaign_term = models.CharField(max_length=100, blank=True, null=True)
    campaign_content = models.CharField(max_length=100, blank=True, null=True)
    campaign_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Play Campaign Url"
        verbose_name_plural = "Play Campaign Urls"

    def __str__(self):
        return f"{self.campaign_name} - {self.ad_network}"
