from apscheduler.schedulers.blocking import BlockingScheduler
from cryptoapp.views import send_email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cryptoscraping.settings')
import django
django.setup()
sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)


def sending_alert_mail():
    print('This job is run every weekday at 8 AM.')
    send_email()
sched.start()