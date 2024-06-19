from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, HTML
from django import forms
from .models import WebCampaignUrl

class CreateWebCampaignUrlForm(forms.ModelForm):
    website_url = forms.URLField()

    class Meta:
        model = WebCampaignUrl
        fields = ['website_url', 'utm_id', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
        labels = {
            'utm_id': 'Campaign ID',
            'utm_source': 'Campaign Source',
            'utm_medium': 'Campaign Medium',
            'utm_campaign': 'Campaign Name',
            'utm_term': 'Campaign Term',
            'utm_content': 'Campaign Content',
        }

    def __init__(self, *args, **kwargs):
        super(CreateWebCampaignUrlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                HTML('<h1>Enter the campaign information</h1>'),
                Div(
                    Field('website_url', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_id', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_source', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_medium', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_campaign', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_term', css_class='form-control', wrapper_class='mb-3'),
                    Field('utm_content', css_class='form-control', wrapper_class='mb-3'),
                ),
                Submit('submit', 'Submit', css_class='btn btn-success'),
                css_class="container"
            )
        )
