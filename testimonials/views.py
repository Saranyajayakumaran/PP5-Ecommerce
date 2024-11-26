from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here

def testimonials_view(request):
    return render(request,'testimonials/testimonials.html')
