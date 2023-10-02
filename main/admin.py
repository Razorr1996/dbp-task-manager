from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Tag, Task

admin.site.register(User, UserAdmin)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = (
        "title",
        "created_at",
        "updated_at",
        "due_to",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )


class TaskInline(admin.TabularInline):
    model = Task.tags.through


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = (
        "id",
        "title",
        "slug",
    )
    readonly_fields = ("id",)
    inlines = (TaskInline,)
