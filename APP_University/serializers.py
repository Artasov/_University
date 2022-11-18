from rest_framework.serializers import ModelSerializer

from .models import *


class AcademicDisciplineSerializer(ModelSerializer):
    class Meta:
        model = AcademicDiscipline
        fields = '__all__'


class DirectionStudySerializer(ModelSerializer):
    class Meta:
        model = DirectionStudy
        fields = '__all__'


class StudyGroupSerializer(ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
