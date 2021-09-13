from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "created_at")
    fields = ("title", "text", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("title", "created_at")
