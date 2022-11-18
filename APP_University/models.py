from datetime import datetime

from django.conf import settings
from django.db import models
from rest_framework.exceptions import ValidationError

from Core.models import User, Task


class Report(models.Model):
    file = models.FileField(upload_to='reports/%Y/%m/%d/')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(default=datetime.now)


class AcademicDiscipline(models.Model):
    name = models.CharField(max_length=300)


class DirectionStudy(models.Model):
    name = models.CharField(max_length=300)
    curator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    disciplines = models.ManyToManyField(AcademicDiscipline, related_name='disciplines')


class StudyGroup(models.Model):
    students = models.ManyToManyField(User, related_name='students')

    def clean(self, *args, **kwargs):
        if self.students.count() >= settings.UNIVERSITY_MAX_GROUP_SIZE:
            raise ValidationError(
                f'A group cannot have more than {settings.UNIVERSITY_MAX_GROUP_SIZE} students.'
            )
        super(StudyGroup, self).clean(*args, **kwargs)