from django import forms
from .models import Testimonial, Product


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['product', 'message']

    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        label="Product",
        widget=forms.Select(attrs={'class': 'border-line'})
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'border-line'})
    )
