from django.db import models

# Create your models here.
class SEOSettings(models.Model):
    APP_CHOICES = [
        ('contact_request', 'Contact Us'),
        ('homepage', 'Homepage'),
        ('playcampaign', 'Play Campaign'),
        ('webcampaign', 'Web Campaign'),
    ]

    app_name = models.CharField(max_length=100, choices=APP_CHOICES, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    keywords = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.app_name} - {self.title}'
    
    
    class Meta:
        verbose_name = "SEO Setting"
        verbose_name_plural = "SEO Settings"