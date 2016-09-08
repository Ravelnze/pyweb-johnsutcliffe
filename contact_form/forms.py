from django import forms
from models import Enquiry


class EnquiryForm(forms.ModelForm):
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
