from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Tag, Task


class TaskManagerAdminSite(admin.AdminSite):
    pass


task_manager_admin_site = TaskManagerAdminSite(name="Task manager admin")


@admin.register(Task, site=task_manager_admin_site)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("-id",)
    list_display = (
        "title",
        "created_at",
        "updated_at",
        "deadline_at",
    )
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
    )


class TaskInline(admin.TabularInline):
    model = Task.tags.through


@admin.register(Tag, site=task_manager_admin_site)
class TagAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_display = (
        "id",
        "title",
        "slug",
    )
    readonly_fields = ("id",)
    inlines = (TaskInline,)


UserAdmin.list_display += ("role",)
UserAdmin.list_filter += ("role",)
UserAdmin.fieldsets += (("Extra Fields", {"fields": ("role",)}),)

task_manager_admin_site.register(User, UserAdmin)
