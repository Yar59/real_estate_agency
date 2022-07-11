from django.contrib import admin

from .models import Flat, Complaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ('created_at',)
    list_display = ('address', 'town', 'price', 'construction_year', 'new_building')
    list_display_links = ('address',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')


@admin.register(Complaint)
class FlatAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')
