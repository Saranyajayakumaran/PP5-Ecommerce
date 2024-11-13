from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    model =Checkout
    fields = ('fullname','email','phone_number',
              'street_address1','street_address2',
              'town_or_city','postcode','country',)
    
def __init__(self,*args, **kwargs):

    super().__init__(*args,**kwargs)
    placeholders = {
        'full_name':'Full Name',
        'email':'Email Address',
        'phone_number':'Phone Number',
        'street_address1':'Street Address 1',
        'street_address2':'Street Address 2',
        'postcode':'Postal Code',
        'town_or_city':'Town or City',
        'country':'Country',
    }

    self.fields['full_name'].widges.arrts['autofocus']=True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder']=placeholder
        self.fields[field].widget.attrs['class']='srtipe-style-input'
        self.fields[field].label=False

    
