from django.contrib import admin
from webapp.models import Tag, Status, Type


@admin.register(Tag)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description']
    list_filter = ['status', 'type']
    search_fields = ['status', 'type',  'id']
    fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Status)
admin.site.register(Type)
