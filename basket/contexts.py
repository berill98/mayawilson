from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package


def basket_contents(request):

    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for package_id, quantity in basket.items():
        package = get_object_or_404(Package, pk=package_id)
        total += package.price
        basket_items.append({
            'package_id': package_id,
            'quantity': quantity,
            'package': package,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context