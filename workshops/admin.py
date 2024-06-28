from django.contrib import admin
from .models import Workshops, WorkshopApply

# Register your models here.

class WorkshopsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'duration',
        'date',
        'time',
        'location',
        'image',
    )

admin.site.register(Workshops)
admin.site.register(WorkshopApply)
