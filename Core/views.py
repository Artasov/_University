import os

from APP_University.permissions import IsAdministrator
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework import mixins, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import User, Task
from .serializers import UserSerializer


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


@api_view()
@permission_classes([IsAdministrator | IsAdminUser])
def TaskStatusAPIView(request, task_id: str):
    if len(task_id) == 0 or not Task.objects.filter(task_id=task_id).exists():
        return Response({
            'Task id is wrong or this task does not exists.'
        }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'task_id': task_id,
        'status': Task.objects.get(task_id=task_id).status
    }, status=status.HTTP_200_OK)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    permission_classes = [IsAdminUser, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
