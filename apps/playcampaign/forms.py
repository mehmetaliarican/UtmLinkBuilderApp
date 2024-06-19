from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, HTML
from .models import PlayCampaignUrl

class CreatePlayCampaignUrlForm(forms.ModelForm):
    class Meta:
        model = PlayCampaignUrl
        fields = ['ad_network', 'application_id', 'campaign_source', 'campaign_medium', 'campaign_term', 'campaign_content', 'campaign_name']
        labels = {
            'ad_network': 'Ad Network',
            'application_id': 'Application ID',
            'campaign_source': 'Campaign Source',
            'campaign_medium': 'Campaign Medium',
            'campaign_term': 'Campaign Term',
            'campaign_content': 'Campaign Content',
            'campaign_name': 'Campaign Name',
        }

    def __init__(self, *args, **kwargs):
        super(CreatePlayCampaignUrlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                HTML('<h1>Enter the campaign information</h1>'),
                Div(
                    Field('ad_network', css_class='form-control', wrapper_class='mb-3'),
                    Field('application_id', css_class='form-control', wrapper_class='mb-3'),
                    Field('campaign_source', css_class='form-control', wrapper_class='mb-3'),
                    Field('campaign_medium', css_class='form-control', wrapper_class='mb-3'),
                    Field('campaign_term', css_class='form-control', wrapper_class='mb-3'),
                    Field('campaign_content', css_class='form-control', wrapper_class='mb-3'),
                    Field('campaign_name', css_class='form-control', wrapper_class='mb-3'),
                ),
                Submit('submit', 'Submit', css_class='btn btn-primary'),
                css_class="container"
            )
        )
