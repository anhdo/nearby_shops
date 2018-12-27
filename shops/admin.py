from django.contrib.gis import admin
from shops.models import Shop

@admin.register(Shop)
class ShopAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'location')
