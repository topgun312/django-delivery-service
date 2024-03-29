from django.contrib import admin
from service.models import Cargo, Car, Location


@admin.register(Cargo)
class CardoAdmin(admin.ModelAdmin):
  ordering = ('pk',)



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
  ordering = ('pk',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  ordering = ('pk',)

