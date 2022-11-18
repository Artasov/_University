from django.urls import path, include
from rest_framework import routers

from . import views
from .views import AdministratorViewSet, CuratorViewSet, AcademicDisciplineViewSet, StudentViewSet, \
    DirectionStudyViewSet, StudyGroupViewSet

administrator = routers.SimpleRouter()
curator = routers.SimpleRouter()
academic_discipline = routers.SimpleRouter()
student = routers.SimpleRouter()
direction_study = routers.SimpleRouter()
study_group = routers.SimpleRouter()

administrator.register(r'administrator', AdministratorViewSet, basename='administrator')
curator.register(r'curator', CuratorViewSet, basename='curator')
academic_discipline.register(r'academic_discipline', AcademicDisciplineViewSet, basename='academic_discipline')
student.register(r'student', StudentViewSet, basename='student')
direction_study.register(r'direction_study', DirectionStudyViewSet, basename='direction_study')
study_group.register(r'study_group', StudyGroupViewSet, basename='study_group')

urlpatterns = [
    path('api/v1/', include(administrator.urls)),
    path('api/v1/', include(curator.urls)),
    path('api/v1/', include(academic_discipline.urls)),
    path('api/v1/', include(student.urls)),
    path('api/v1/', include(direction_study.urls)),
    path('api/v1/', include(study_group.urls)),
]

urlpatterns += [
    path('api/v1/generate_report/', views.GenerateReportAPIView, name='generate_report'),
    path('api/v1/report_status/<str:task_id>', views.ReportStatusAPIView, name='report_status'),
]
