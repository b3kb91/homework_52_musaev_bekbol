from django.contrib import admin

from webapp.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_completion']
    list_filter = ['status', 'id']
    list_display_links = ["description"]
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'date_completion']
    readonly_fields = ['date_completion']


admin.site.register(ToDo, ToDoAdmin)
