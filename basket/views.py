from django.shortcuts import render, redirect, reverse

# Create your views here.
def add_to_basket(request, package_id):
    """ Add a package to the basket """

    quantity = int(1),
    date = request.POST.get('photodate')
    basket = request.session.get('basket', {})
    redirect_url = request.POST.get('redirect_url')

    basket[package_id] = quantity 
    request.session['basket'] = basket  
    print(basket)
    return redirect(reverse('checkout'))