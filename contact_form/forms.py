from django import forms
from models import Enquiry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, HTML, Field
from crispy_forms.bootstrap import StrictButton


class EnquiryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'First'
        self.fields['last_name'].label = 'Last'
        self.fields['email_contact'].label = 'Email Address'
        self.fields['phone_contact'].label = 'Phone Number'
        self.fields['wedding_date'].label = 'Wedding Date'
        self.fields['comments'].label = 'Comments/Questions'
        self.helper = FormHelper()
        self.helper.form_id = 'id_contact_form'
        self.helper.form_method = 'POST'
        self.helper.form_class = 'lower-pad'
        self.helper.layout = Layout(
            Fieldset(
                'Send John an enquiry for an obligation free quote:',
                HTML(
                    '<label class="control-label">Name:</label>',
                ),
                Div(
                    'first_name',
                    'last_name',
                    css_class='form-inline'
                ),
                'email_contact',
                Field('phone_contact', placeholder='0412345678'),
                Field('venue', placeholder='Venue Name'),
                Field('wedding_date', placeholder='01/01/2000'),
                Field('comments', placeholder='Is there anything else you would like to know?')
            ),
            ButtonHolder(
                StrictButton('Submit', css_class='btn-default', type='submit')
            ),
        )

    class Meta:
        model = Enquiry
        fields = [
            'first_name',
            'last_name',
            'email_contact',
            'phone_contact',
            'venue',
            'wedding_date',
            'comments'
        ]
