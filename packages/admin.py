from django.contrib import admin
from .models import Package


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'description',
        'duration',
        'photo_count',
    )

    ordering = ('price',)


admin.site.register(Package, PackageAdmin)
