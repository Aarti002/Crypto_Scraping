# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptoscraping.settings')

# create a Celery instance and configure it using the settings from Django
app = Celery('cryptoscraping',broker='redis://127.0.0.1:6379')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-email-task-crontab': {
        'task': 'cryptoapp.tasks.send_update_email',
        'schedule': crontab(hour=20, minute=0, day_of_week=1),
    },
}