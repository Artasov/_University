from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class UserType(models.TextChoices):
        administrator = 'administrator', _('Administrator')
        curator = 'curator', _('Curator')
        student = 'student', _('Student')

    class Gender(models.TextChoices):
        M = 'M', _('M')
        W = 'W', _('W')

    gender = models.CharField(max_length=50, choices=Gender.choices, default=Gender.M)
    user_type = models.CharField(max_length=50, choices=UserType.choices, default=UserType.student)

    def isAdministrator(self):
        if self.user_type.lower() == self.UserType.administrator:
            return True
        return False

    def isCurator(self):
        if self.user_type.lower() == self.UserType.curator:
            return True
        return False

    def isStudent(self):
        if self.user_type.lower() == self.UserType.student:
            return True
        return False

    def __str__(self):
        return f'{self.username}, {self.gender}, {self.user_type}'


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        running = 'running', _('running')
        finished = 'finished', _('finished')
        error = 'error', _('error')
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=TaskStatus.choices, default=TaskStatus.running)
    task_id = models.CharField(max_length=36, blank=True, null=True, default=None)
    temp_task_id = models.IntegerField(blank=True, null=True, default=None)
    date_start = models.DateTimeField(default=datetime.now)
    date_finished = models.DateTimeField(blank=True, null=True)
