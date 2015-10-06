from django.contrib.gis import admin

from osm.models import Banks

class BanksAdmin(admin.OSMGeoAdmin):
    list_display = ('name',)
    order_by = ('name',)


admin.site.register(Banks, BanksAdmin)
