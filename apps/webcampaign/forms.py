from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, HTML
from django import forms
from .models import WebCampaignUrl

class CreateWebCampaignUrlForm(forms.ModelForm):
    website_url = forms.URLField()

    class Meta:
        model = WebCampaignUrl
        fields = ['website_url',  'utm_source', 'utm_medium', 'utm_term', 'utm_content']
        labels = {
            'website_url': 'Website Url',
            'utm_source': 'Campaign Source',
            'utm_medium': 'Campaign Medium',
            'utm_term': 'Campaign Term',
            'utm_content': 'Campaign Content',
        }

    def __init__(self, *args, **kwargs):
        super(CreateWebCampaignUrlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                HTML('<h5>Enter the campaign information</h5>'),
                Div(
                    Field('website_url', css_class='validate', wrapper_class='input-field'),
                    Field('utm_source', css_class='validate', wrapper_class='input-field'),
                    Field('utm_medium', css_class='validate', wrapper_class='input-field'),
                    Field('utm_term', css_class='validate', wrapper_class='input-field'),
                    Field('utm_content', css_class='validate', wrapper_class='input-field'),
                ),
                Submit('submit', 'Get Link', css_class='btn waves-effect waves-light deep-orange lighten-1'),
                css_class="container mt-2"
            )
        )
