from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    readonly_fields = ('query_number', 'email_date')

    fields = ('query_number', 'email_date', 'first_name', 'surname',
              'email', 'subject', 'query', 'hearfrom')

    list_display = ('query_number', 'email_date', 'subject', 'first_name')

    ordering = ('-email_date',)

admin.site.register(Contact, ContactAdmin)