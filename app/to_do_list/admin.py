from django.contrib import admin

from to_do_list.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "status", "created_at")
    list_filter = ("id", "description", "status", "created_at")
    search_fields = ("description", "status")
    fields = ("description", "status", "created_at")
    readonly_fields = ("id", "created_at")


admin.site.register(ToDo, ToDoAdmin)
