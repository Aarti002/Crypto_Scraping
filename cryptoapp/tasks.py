import requests
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags

from .models import SubscribedUsers

from celery import shared_task
from time import sleep

@shared_task

def sending_crypto_info(self):

    apidata = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false').json()
    curr_pri = apidata[0]["current_price"]
    subject = 'Notification Mail'
    message = 'Subscribe to our website to know latest updates!'
    # html_template='/index.html'
    html_message = render_to_string('index.html', {'apidata': apidata})
    plain_message = strip_tags(html_message)
    subscribed = SubscribedUsers.objects.filter(yes_no=True)
    ans = subscribed.values('email')
    print(ans)
    receivers = []
    for rec in ans:
        receivers.append(rec['email'])
    print(receivers)
    try:

        send_mail(subject, message, 'aartikumarisingh120@gmail.com', receivers, html_message=html_message)
       # messages.success(request, "Message Delivered!")
        print('successfully sent the mail')
    except:
        #messages.error(request, "Message not delivered!")
        print('Not sent the mail')

