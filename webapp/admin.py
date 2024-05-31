from django.contrib import admin
from webapp.models import Tag, Status, Type, Projects


admin.site.register(Tag)
admin.site.register(Projects)
admin.site.register(Status)
admin.site.register(Type)
