from django.shortcuts import render


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, package_id):
    """ Add a package to the basket """

    quantity = int(1),
    basket = request.session.get('basket', {})

    basket[package_id] = quantity

    request.session['basket'] = basket
    return render(request, 'basket/basket.html')


def remove_from_basket(request, package_id):
    """Remove the item from the basket"""

    try:
        package = get_object_or_404(Package, pk=package_id)
        basket = request.session.get('basket', {})

        bag.pop(package_id)
        messages.success(request, f'Removed {package.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
