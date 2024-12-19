import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simpledjango_with_mongoDB.settings')

app = Celery('simpledjango_with_mongoDB')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
