from django import forms
from models import Enquiry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, HTML, Field
from crispy_forms.bootstrap import StrictButton


class EnquiryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['email_contact'].label = ''
        self.fields['phone_contact'].label = ''
        self.fields['venue'].label = ''
        self.fields['wedding_date'].label = ''
        self.fields['comments'].label = ''
        self.helper = FormHelper()
        self.helper.form_id = 'id_contact_form'
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Fieldset(
                'Send John an enquiry for an obligation free quote:',
                HTML(
                    '<label class="control-label">Name</label>',
                ),
                Div(
                    Field('first_name', placeholder='First Name'),
                    Field('last_name', placeholder='Last Name'),
                    css_class='form-inline'
                ),
                HTML(
                    '<br />'
                    '<label class="control-label">Contact Details</label>',
                ),
                Div(
                    Field('email_contact', placeholder='Email Address'),
                    Field('phone_contact', placeholder='Phone Number'),
                    css_class='form-inline'
                ),
                HTML(
                    '<br />'
                    '<label class="control-label">Wedding Details</label>',
                ),
                Div(
                    Field('venue', placeholder='Venue Name'),
                    Field('wedding_date', placeholder='Wedding Date'),
                    # Field('wedding_date', template='datepicker.html'),
                    css_class='form-inline'
                ),
                HTML(
                    '<br />'
                    '<label class="control-label">Comments/Questions</label>',
                ),
                Field('comments', placeholder='Anything else you would like to know?')
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
