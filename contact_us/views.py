from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactEnquiryForm


def contact_enquiry_view(request):
    """
    This view allows the user to submit
    an enquiry through the contact form.
    If the form is valid, it saves the enquiry
    and displays a success message.
    If the form is not valid, it shows an error
    message and prompts the user to try again.
    """
    if request.method == 'POST':
        form = ContactEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us!'
                             'We have received your inquiry.')
            return redirect('contact_us')
        else:
            messages.error(request, 'There was an error with '
                           'your submission. Please try again.')
    else:
        form = ContactEnquiryForm()

    context = {
        'form': form,
        'only_success_message': True, 
    }

    return render(request, 'contact_us/contact_us.html', context)
