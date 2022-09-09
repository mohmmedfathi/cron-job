import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

app = Celery('celery_')

app.config_from_object('django.conf:settings')



app._autodiscover_tasks(lambda:settings.INSTALLED_APPS,related_name='ds')

app.conf.beat_schedule  = {
    'add-every-2-hour':{
        'task':'send_notification',
        'schedule' : crontab(minute='*/1')
    }
}