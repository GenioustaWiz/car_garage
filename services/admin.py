
# admin.py
from django.contrib import admin
from .models import *

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'service', 'timestamp')
    list_filter = ('date', 'service', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'service')
    readonly_fields = ('timestamp',)

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'cat_description','img_icon')
    search_fields = ('category_name',)

@admin.register(ServiceOffered)
class ServiceOfferedAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_name', 'description', 'category', )
    list_filter = ('category',)
    search_fields = ('service_name', 'category__category_name')