from django.contrib import admin
from django.contrib.admin import display

from .models import *


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['task', 'file', 'date_created']


@admin.register(AcademicDiscipline)
class AcademicDisciplineAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(DirectionStudy)
class DirectionStudyAdmin(admin.ModelAdmin):
    list_display = ['name', 'curator']


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'count_students']

    @display()
    def count_students(self, obj: StudyGroup):
        return obj.students.count()