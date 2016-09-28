from django import forms
from models import Enquiry
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, HTML, Field
from crispy_forms.bootstrap import StrictButton
from johnsutcliffe.settings import DATE_INPUT_FORMATS


class EnquiryForm(forms.ModelForm):
    wedding_date = forms.DateField(input_formats=DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        super(EnquiryForm, self).__init__(*args, **kwargs)
        # Helper definition
        self.helper = FormHelper()
        self.helper.form_id = 'id_contact_form'
        self.helper.form_method = 'POST'
        self.helper.form_show_labels = False
        self.helper.form_class = 'lower-pad'
        self.helper.layout = Layout(
            Fieldset(
                'Send John an enquiry for an obligation free quote',
                HTML(
                    '<label class="control-label">Name</label>',
                ),
                Div(
                    Field('first_name', placeholder='First Name', template='dynamic_text_input.html',
                          css_class='input-required'),
                    Field('last_name', placeholder='Last Name', template='dynamic_text_input.html',
                          css_class='input-required'),
                    css_class='row'
                ),
                HTML(
                    '<label class="control-label">Contact Details</label>',
                ),
                Div(
                    Field('email_contact', placeholder='Email Address', template='dynamic_text_input.html',
                          css_class='input-required'),
                    Field('phone_contact', placeholder=' Phone Number', template='dynamic_text_input.html'),
                    css_class='row'
                ),
                HTML(
                    '<label class="control-label">Wedding Details</label>',
                ),
                Div(
                    Field('venue', placeholder=' Venue Name', template='dynamic_text_input.html'),
                    Field('wedding_date', placeholder=' Wedding Date', readonly="True",
                          template='dynamic_text_input.html'),
                    css_class='row'
                ),
                HTML(
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
