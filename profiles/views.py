from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
