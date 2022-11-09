from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'order_total', 'original_basket', 
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'order_total', 'original_basket', 
              'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)