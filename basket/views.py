from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
def add_to_basket(request, package_id):
    """ Add a package to the basket """

    date = request.POST.get('photodate')

    basket = request.session.get('basket', {})
    redirect_url = request.POST.get('redirect_url')

    request.session['basket'] = {f'{package_id}': date} 
    messages.success(request, 'Successfully added to the basket!')
    return redirect(reverse('checkout'))