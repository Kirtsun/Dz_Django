from django.contrib import admin

from .models import MiddleWare


@admin.register(MiddleWare)
class MiddleAdmin(admin.ModelAdmin):
    list_display = ("path", "method", "timestamp", "json")
    fieldsets = [
        ('Path', {'fields': ['path']}),
        ('Method', {'fields': ['method']}),
        ('request data', {'fields': ['json']}),
    ]
    list_display_links = ('path', 'timestamp', 'json', )
    list_filter = ['method', 'timestamp']
    list_editable = ['method']
    search_fields = ['path']
    date_hierarchy = 'timestamp'
    list_per_page = 10
    save_as = True
