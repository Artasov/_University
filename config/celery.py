import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config',
             broker=f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0',
             include=['APP_University.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()