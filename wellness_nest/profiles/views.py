from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from payment.models import Checkout

# Create your views here.
def profile_view(request):
    """Display User profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form' : form,
        'orders' : orders,
        'on_profile_page' : True,
    }

    return render(request, template, context)

def order_history_view(request,order_number):
    """"""

    order = get_object_or_404(Checkout, order_number=order_number)

    messages.info(request,(
        f'This is a past confrimation for order number {order_number}.'
        'A confirmation email was sent on date of the order'
    ))

    template = 'payment/payment_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

