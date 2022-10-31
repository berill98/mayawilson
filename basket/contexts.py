from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from packages.models import Package


def basket_contents(request):

    basket_items = []
    total = 0

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context