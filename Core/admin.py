from django.contrib import admin

# Register your models here.
from .models import User, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'user_type']
    list_editable = ['user_type']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'task_id', 'date_start', 'date_finished']
