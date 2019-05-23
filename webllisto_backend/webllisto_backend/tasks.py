from __future__ import absolute_import, unicode_literals
from celery import Celery
from app.utils import send_contact_email

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context


app = Celery('tasks', broker='amqp://localhost',backend='amqp://localhost')

@app.task
def send_contact_email(data):        
    subject = loader.render_to_string('contact_form_subject.txt')    
    subject = ''.join(subject.splitlines())   
    body = loader.render_to_string('contact_form.html',data) #render with dynamic data  
    
    email_message = EmailMultiAlternatives(subject, str(body), settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
    email_message.attach_alternative(body,"text/html")# attach the HTML version
    email_message.send()
