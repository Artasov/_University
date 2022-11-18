from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from rest_framework import routers

from . import views
from .views import UserViewSet

user_router = routers.SimpleRouter()
user_router.register(r'users', UserViewSet)
from config.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('accounts/', include('rest_framework.urls')),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/task_status/<str:task_id>/', views.TaskStatusAPIView, name='task_status'),
    path('', include('APP_University.urls')),
    path('docs/', RedirectView.as_view(url='/swagger/'), name='docs'),
    path('', RedirectView.as_view(url='/docs/')),
    re_path(r'download/(?P<path>.*)$', views.download, name='download'),
]
urlpatterns += doc_urls
