from django.contrib import admin
from .models import Todo


# Register your models here.

@admin.action(description="Hard Delete")
def hard_delete(modeladmin, request, queryset):
    queryset.delete()


@admin.action(description="Soft Delete")
def soft_delete(modeladmin, request, queryset):
    queryset.update(is_deleted=True)


@admin.action(description="Restore selected todos")
def restore(modeladmin, request, queryset):
    queryset.update(is_deleted=False)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'is_complete', 'is_deleted')
    list_filter = ('owner', 'is_complete', 'is_deleted')
    actions = [hard_delete, soft_delete, restore]
