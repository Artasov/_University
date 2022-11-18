from random import choice

from APP_University.models import StudyGroup, AcademicDiscipline, DirectionStudy
from Core.models import User
from django.core.management.base import BaseCommand
from django.db import transaction


class Command(BaseCommand):
    help = 'Initialization test users'

    def handle(self, *args, **options):
        with transaction.atomic():
            if User.objects.filter(username='admin', is_staff=True).exists():
                print('Test case already created.')
                return
            User.objects.create_superuser(username='admin', password="1")
            User.objects.create_user(username='a1', password="1", user_type=User.UserType.administrator)

            for i in range(50):
                User.objects.create_user(username=f's{i}',
                                         password="1",
                                         gender=choice([User.Gender.M, User.Gender.W]))
            for i in range(4):
                StudyGroup.objects.create()

            group1 = StudyGroup.objects.all()[0]
            group2 = StudyGroup.objects.all()[1]
            group3 = StudyGroup.objects.all()[2]
            for i in range(20):
                group1.students.add(User.objects.all()[i])
            for i in range(20, 40):
                group2.students.add(User.objects.all()[i])
            for i in range(40, 50):
                group3.students.add(User.objects.all()[i])

            academic_disciplineMath = AcademicDiscipline.objects.create(name='Math')
            academic_disciplineGeography = AcademicDiscipline.objects.create(name='Geography')
            academic_disciplineChemistry = AcademicDiscipline.objects.create(name='Chemistry')
            academic_disciplinePhysics = AcademicDiscipline.objects.create(name='Physics')
            academic_disciplineBiology = AcademicDiscipline.objects.create(name='Biology')

            direction_study1 = DirectionStudy.objects.create(name='Applied Mathematics and Computer science')
            direction_study2 = DirectionStudy.objects.create(name='Mathematics and Computer Science')

            direction_study1.disciplines.add(academic_disciplineMath)
            direction_study1.disciplines.add(academic_disciplineGeography)
            direction_study1.disciplines.add(academic_disciplineChemistry)

            direction_study2.disciplines.add(academic_disciplineMath)
            direction_study2.disciplines.add(academic_disciplinePhysics)
            direction_study2.disciplines.add(academic_disciplineBiology)

            curator1 = User.objects.create_user(username='c1', password="1", user_type=User.UserType.curator)
            curator2 = User.objects.create_user(username='c2', password="1", user_type=User.UserType.curator)
            direction_study1.curator = curator1
            direction_study2.curator = curator2
            direction_study1.save()
            direction_study2.save()

            print('Test case created successfully.')
