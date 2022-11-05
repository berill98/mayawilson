from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    #basket = request.session.get('basket', {})
    #if not bag:
    #    messages.error(request, "There's nothing in your bag at the moment")
    #    return redirect(reverse('packages'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)


def add_to_basket(request, package_id):
    """ Add a package to the basket """

    quantity = int(1),
    date = request.POST.get('photodate')
    basket = request.session.get('basket', {})

    basket[package_id] = quantity 
    request.session['basket'] = basket  
    print(basket)
    return render(request, 'checkout/checkout.html')