from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("title", "deadline", "is_done")
    search_fields = ("title", "description")
    list_filter = ("deadline", "is_done")
    date_hierarchy = "created"


admin.site.register(Todo, TodoAdmin)
