from django.contrib import admin

# Register your models here.
from base.models import Country, Region


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)


admin.site.register(Country, CountryAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name',)


admin.site.register(Region, RegionAdmin)
