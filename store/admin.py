from django.contrib import admin
from .models import *

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display=['length','width', 'height','area','volume','created_by','created_on','last_updated']
    readonly_fields = ['area','volume']
