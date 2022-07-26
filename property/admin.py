from django.contrib import admin

from .models import Flat, Complaint, Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ('created_at',)
    list_display = (
        'address',
        'town',
        'price',
        'construction_year',
        'new_building',
    )
    list_display_links = ('address',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat')


@admin.register(Owner)
class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('name', 'pure_number')
    raw_id_fields = ('flats',)
    list_display = ('name', 'pure_number',)
    list_display_links = ('name',)
