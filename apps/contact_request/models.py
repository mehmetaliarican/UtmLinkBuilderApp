from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Validators for phone numbers
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)

class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)  # Use EmailField for email validation
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Add phone number validation
    landline = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Add phone number validation
    created = models.DateTimeField(default=timezone.now)  # Set default to current date and time
    isHandled = models.BooleanField(default=False)  # Set default to False
    
    class Meta:
        verbose_name = "Contact Request"
        verbose_name_plural = "Contact Requests"
    
    def __str__(self) -> str:
        return self.name + " " + self.surname