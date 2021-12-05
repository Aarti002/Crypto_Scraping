from apscheduler.schedulers.blocking import BlockingScheduler
from cryptoapp.views import send_email
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cryptoscraping.settings')
import django
django.setup()
sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes.')
    send_email()

@sched.scheduled_job('cron', day_of_week='mon-sat', hour=17)
def scheduled_job():
    print('This job is run every weekday at 5pm.')


sched.start()