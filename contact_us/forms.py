from django import forms
from .models import ContactEnquiry


class ContactEnquiryForm(forms.ModelForm):

    BANNED_KEYWORDS = [
        'disgusting', 'annoying', 'pathetic', 'terrible', 'awful', 'horrible','ridiculous',
        'absurd','lame','trivial'
    ]
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

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name) < 3:
            raise forms.ValidationError("Full name must be at least 3 characters long.")
        if not full_name.replace(" ", "").isalpha():
            raise forms.ValidationError("Full name should only contain letters and spaces.")
        return full_name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if len(subject) < 5:
            raise forms.ValidationError("Subject must be at least 5 characters long.")
        return subject

    def clean_message(self):
            message = self.cleaned_data.get('message')
            if len(message) < 20:
                raise forms.ValidationError("Message must be at least 20 characters long.")
            for word in self.BANNED_KEYWORDS:
                if word in message.lower():
                    raise forms.ValidationError(f"Your message contains inappropriate content: '{word}'.")
            return message