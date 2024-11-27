from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from .forms import ContactEnquiryForm

# Create your views here.

def contact_enquiry_view(request):
    if request.method == 'POST':
        form = ContactEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! We have received your inquiry.')
            return redirect('contact_us')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactEnquiryForm()

    return render(request, 'contact_us/contact_us.html', {'form':form})
