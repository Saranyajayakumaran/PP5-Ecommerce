from django.shortcuts import render

# Create your views here.

def contact_enquiry_view(request):
    return render(request, 'contact_us/contact_us.html')
