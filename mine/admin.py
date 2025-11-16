from django.contrib import admin
from .models import BestTime

@admin.register(BestTime)
class BestTimeAdmin(admin.ModelAdmin):
    list_display = ['difficulty', 'time_seconds', 'created_at']
    list_filter = ['difficulty', 'created_at']
    ordering = ['difficulty', 'time_seconds']