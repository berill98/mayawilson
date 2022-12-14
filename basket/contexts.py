
from django.shortcuts import get_object_or_404
from packages.models import Package


def basket_contents(request):

    basket_items = []
    total = 0
    basket = request.session.get('basket', {})

    for item_id, date in basket.items():
        package = get_object_or_404(Package, pk=item_id)
        total = package.price
        basket_items.append({
                'item_id': item_id,
                'package': package,
                'date': date,
            })

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
