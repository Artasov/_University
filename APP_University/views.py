from random import randrange

from Core.models import Task
from Core.models import User
from Core.serializers import UserSerializer
from rest_framework import mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .permissions import *
from .serializers import *
from .tasks import GenerateReportTask


@api_view()
@permission_classes([IsAdministrator | IsAdminUser])
def ReportStatusAPIView(request, task_id: str):
    if len(task_id) == 0 or not Task.objects.filter(task_id=task_id).exists():
        return Response({
            'Task id is wrong or this task does not exists.'
        }, status=status.HTTP_404_NOT_FOUND)
    if Report.objects.filter(task=Task.objects.get(task_id=task_id)).exists():
        return Response({
            'task_id': task_id,
            'task_status': Task.objects.get(task_id=task_id).status,
            'download_report': reverse("download",
                                       args=[
                                           str(Report.objects.get(task=Task.objects.get(task_id=task_id)).
                                               file.url).replace(settings.MEDIA_URL, '')],
                                       request=request)
        }, status=status.HTTP_200_OK)
    return Response({
        'task_id': task_id,
        'task_status': Task.objects.get(task_id=task_id).status,
        'download_report': 'Task is not finished'
    }, status=status.HTTP_200_OK)


@api_view()
@permission_classes([IsAdministrator | IsAdminUser])
def GenerateReportAPIView(request):
    temp_task_id = randrange(1000000, 9999999)
    task = Task.objects.create(name=GenerateReportTask.__name__, temp_task_id=temp_task_id)
    res = GenerateReportTask.delay(temp_task_id)
    task.task_id = res.task_id
    task.save()

    return Response({
        'success': 'Report generation started.',
        'check_report_status': f'{reverse("report_status", args=[task.task_id], request=request)}',
    }, status=status.HTTP_200_OK)


class ReportViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    permission_classes = [IsAdministrator | IsAdminUser]
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class AdministratorViewSet(ModelViewSet):
    permission_classes = [IsAdminUser | IsAdminUser]
    queryset = User.objects.filter(user_type=User.UserType.administrator)
    serializer_class = UserSerializer


class CuratorViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     # mixins.DestroyModelMixin,
                     # Мне, кажется, что пользователей удалять "Администратор" не может.
                     mixins.ListModelMixin,
                     GenericViewSet):
    permission_classes = [IsAdministrator | IsAdminUser]
    queryset = User.objects.filter(user_type=User.UserType.curator)
    serializer_class = UserSerializer


class StudentViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     # mixins.DestroyModelMixin,
                     # Мне, кажется, что пользователей удалять куратор не может.
                     mixins.ListModelMixin,
                     GenericViewSet):
    permission_classes = [IsCurator | IsAdminUser]
    queryset = User.objects.filter(user_type=User.UserType.student)
    serializer_class = UserSerializer


class AcademicDisciplineViewSet(ModelViewSet):
    permission_classes = [IsAdministrator | IsAdminUser]
    queryset = AcademicDiscipline.objects.all()
    serializer_class = AcademicDisciplineSerializer


class DirectionStudyViewSet(ModelViewSet):
    permission_classes = [IsAdministrator | IsAdminUser]
    queryset = DirectionStudy.objects.all()
    serializer_class = DirectionStudySerializer


class StudyGroupViewSet(ModelViewSet):
    permission_classes = [IsCurator | IsAdminUser]
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
