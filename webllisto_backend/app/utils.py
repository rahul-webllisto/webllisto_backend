from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import loader, Context

def send_contact_email(data):
    subject = loader.render_to_string('contact_form_subject.txt')    
    subject = ''.join(subject.splitlines())   
    body = loader.get_template('contact_form.html')
    c = Context(data)
    template_data = body.render(c['data'])
    # import pdb;pdb.set_trace()   
    email_message = EmailMultiAlternatives(subject, template_data, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
    email_message.send()