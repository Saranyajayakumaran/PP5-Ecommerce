from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TestimonialForm
from .models import Testimonial

# Create your views here

def testimonials_view(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request,'testimonials/testimonials.html',{'testimonials':testimonials})

@login_required
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

@login_required
def delete_testimonials_view(request,testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)
    
    if testimonial.user != request.user and not request.user.is_superuser:
        messages.warning("You dont have permission to delete this testimonial")
        return redirect('testimonials')

    testimonial.delete()
    messages.success(request, "Testimonial deleted successfully.")
    return redirect('testimonials')


@login_required
def  edit_testimonials_view(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, id=testimonial_id)

    if testimonial.user != request.user and not request.user.is_superuser:
        messages.warning("You dont have permission to delete this testimonial")
        return redirect('testimonials')
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Your testimonial has been updated successfully!")
            return redirect('testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'testimonials/update_testimonials.html', {'form': form, 'testimonial': testimonial})
