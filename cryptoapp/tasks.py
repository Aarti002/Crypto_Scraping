from time import sleep
from django.core.mail import send_mail
from .models import *
from celery import shared_task
from django.conf import settings

@shared_task
def send_update_email():
    sleep(20)       #so that our application don't send multiple mails in short period of time [spamming]
    subject="Exiciting Updates!"
    content=f"""
            Dear User,
            We hope this message finds you well. We're thrilled to share some exciting news with you. 
            There are some new coin having current price closer to its ATH/ATL. Do cosider checking!
            Explore the latest updates by visiting {settings.ALLOWED_HOSTS[0]}:8000. 

            Thank you for being a valued member of our community. 
            Your continued support and feedback inspire us to enhance your experience on our platform.

            Feel free to reach out if you have any questions or feedback. Happy browsing!

            Best regards,
            CMS Team
        """
    all_profiles=Profile.objects.filter(is_verified=True)
    emails_list=[]
    for item in all_profiles:
        emails_list.append(item.email)
    send_mail(
        subject,
        content,
        "support@cmsteam.com",
        emails_list,
        fail_silently=False,
    )


@shared_task
def send_verification_email(user_id, user_email):
    sleep(20)  
    subject="Welcome"
    content=f"""
            Hi there,
            We hope this message finds you well. Thank you so much for trusting in us!
            Please verify your account by clicking on this link: {settings.ALLOWED_HOSTS[0]}:8000/verify_user/{user_id}

            Thank you for being a valued member of our community. 
            
            Feel free to reach out if you have any questions or feedback. Happy browsing!

            Best regards,
            CMS Team
        """
    
    send_mail(
        subject,
        content,
        "support@cmsteam.com",
        [user_email,],
        fail_silently=False,
    )