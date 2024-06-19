# contact_request/forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit,HTML
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'surname', 'email', 'mobile', 'landline']
    
    def __init__(self, *args, **kwargs):
        super(ContactRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
           Div(
                HTML('<h1>Leave a message</h1>'),
                Div(
                Field('name', css_class='form-control', wrapper_class='mb-3'),
                Field('surname', css_class='form-control', wrapper_class='mb-3'),
                Field('email', css_class='form-control', wrapper_class='mb-3'),
                Field('mobile', css_class='form-control', wrapper_class='mb-3'),
                Field('landline', css_class='form-control', wrapper_class='mb-3'),
            ),
            Submit('submit', 'Submit', css_class='btn btn-secondary'),
            css_class="container"
           )
        )
