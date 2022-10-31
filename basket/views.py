from django.shortcuts import render


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, package_id):
    """ Add a package to the shopping bag """

    quantity = int(request.POST.get('quantity')),
    basket = request.session.get('basket', {})

    basket[package_id] = quantity

    request.session['basket'] = basket
    return render(request, 'basket/basket.html')
