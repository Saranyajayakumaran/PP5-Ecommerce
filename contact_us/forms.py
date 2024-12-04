from django import forms
from .models import ContactEnquiry


class ContactEnquiryForm(forms.ModelForm):
    class Meta:
        model = ContactEnquiry
        fields = ['full_name', 'email', 'enquiry_type', 'subject', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'border-line'}),
            'email': forms.EmailInput(attrs={'class': 'border-line'}),
            'enquiry_type': forms.Select(attrs={'class': 'border-line'}),
            'subject': forms.TextInput(attrs={'class': 'border-line'}),
            'message': forms.Textarea(attrs={'class': 'border-line'}),
        }
