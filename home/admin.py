from django.contrib import admin
from .models import CarDetail, Cars, CarBrand, CarPhotoList
from django.contrib.auth.models import Group

# Register your models here.


class CarsAdminModel(admin.ModelAdmin):
    list_display = ('brand', 'name', 'year', 'price')
    list_filter = ('created', 'modified')


class CarDetailAdmin(admin.ModelAdmin):
    list_display = ('detail_name', 'brand', 'price', 'count')
    list_filter = ('created', 'modified')
    search_fields = ('detail_name',)


class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)


admin.site.register(CarDetail, CarDetailAdmin)
admin.site.register(Cars, CarsAdminModel)
admin.site.register(CarBrand, CarBrandAdmin)
admin.site.unregister(Group)
admin.site.register(CarPhotoList)
