from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package

from .views import add_to_basket


def basket_contents(request):

    basket_items = []
    total = 0
    basket = request.session.get('basket', {})
    date = request.POST.get('photodate')

    for item_id, quantity in basket.items():
        package = get_object_or_404(Package, pk=item_id)
        total = package.price
        basket_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'package': package,
                'date': date,
            })

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context