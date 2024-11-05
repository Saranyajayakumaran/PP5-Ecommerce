from django import forms

class SortForm(forms.Form):
    SORT_OPTIONS = (
        ('None_None', 'Sort by...'),
        ('price_low_high', 'Price (low to high)'),
        ('price_high_low', 'Price (high to low)'),
        ('rating_low_high', 'Rating (low to high)'),
        ('rating_high_low', 'Rating (high to low)'),
        ('name_az', 'Name (A to Z)'),
        ('name_za', 'Name (Z to A)'),
    )

    sort = forms.ChoiceField(choices=SORT_OPTIONS, required=False)