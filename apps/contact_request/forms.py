# contact_request/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit,HTML
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'surname', 'email', 'mobile', 'companyWebSite']
        labels = {
            'companyWebSite': 'Company website'
        }
    
    def __init__(self, *args, **kwargs):
        super(ContactRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
           Div(
                HTML('<h5>Let us call you</h5>'),
                Div(
                Field('name', css_class='validate', wrapper_class='input-field'),
                Field('surname', css_class='validate', wrapper_class='input-field'),
                Field('email', css_class='validate', wrapper_class='input-field'),
                Field('mobile', css_class='validate', wrapper_class='input-field'),
                Field('companyWebSite', css_class='validate', wrapper_class='input-field'),
            ),
            Submit('submit', 'Send', css_class='btn waves-effect waves-light  deep-orange lighten-1'),
            css_class="container"
           )
        )
