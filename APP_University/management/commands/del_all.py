from random import choice

from APP_University.models import StudyGroup, AcademicDiscipline, DirectionStudy
from Core.models import User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Clearing all models'

    def handle(self, *args, **options):
        with transaction.atomic():
            User.objects.all().delete()
            StudyGroup.objects.all().delete()
            AcademicDiscipline.objects.all().delete()
            DirectionStudy.objects.all().delete()

            print('Deleted success.')
