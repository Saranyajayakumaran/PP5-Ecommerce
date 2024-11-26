from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here

def testimonials_view(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request,'testimonials/testimonials.html',{'testimonials':testimonials})

def add_testimonials_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(request, 'Your testimonial has been added successfully!')
            return redirect('testimonials')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/add_testimonials.html', {'form': form})
