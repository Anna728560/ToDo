from django.contrib import admin
from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "created_datetime", "deadline_datetime", "is_done")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
