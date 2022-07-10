from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'town', 'price', 'construction_year', 'new_building')
    list_display_links = ('address',)
    list_editable = ('new_building',)
