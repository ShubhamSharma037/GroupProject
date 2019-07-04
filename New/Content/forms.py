from django import forms
from .models import ContactFormModel


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactFormModel
        fields = ('vw_name', 'vw_email', 'vw_subject', 'vw_msg')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vw_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Name'})
        self.fields['vw_email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Your Email'})
        self.fields['vw_subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subject'})
        self.fields['vw_msg'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Message'})




