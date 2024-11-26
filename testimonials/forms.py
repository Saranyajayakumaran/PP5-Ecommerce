from django import forms
from .models import Testimonial,Products

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['product','message']

    product = forms.ModelChoiceField(
        queryset=Products.objects.all(),
        label="Product",
        widget=forms.Select(attrs={'class':'form-controm'}))