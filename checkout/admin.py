from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_basket', 
                       'stripe_pid')

    list_display = ('order_number', 'date', 'photodate', 'full_name',
                    'order_total',)

    ordering = ('-photodate',)

admin.site.register(Order, OrderAdmin)