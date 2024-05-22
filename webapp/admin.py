from django.contrib import admin
from webapp.models import Tag, Status, Type, Projects


@admin.register(Tag)
class TasksAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description']
    list_filter = ['status', 'type']
    search_fields = ['status', 'type', 'id']
    fields = ['summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_filter = ['id', 'name']
    search_fields = ['name', 'description']
    fields = ['name', 'description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Status)
admin.site.register(Type)
