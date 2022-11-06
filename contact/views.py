from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'surname': request.POST['surname'],
            'email': request.POST['email'],
            'subject': request.POST['subject'],
            'query': request.POST['query'],
           'hearfrom': request.POST['hearfrom']
        }
        contact_form = ContactForm(form_data)

    contact_form = ContactForm()
    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
        
    #send_confirmation_email(user_contact)


def send_confirmation_email(user_contact):
    """Send the user a confirmation email"""
    cust_email = user_contact.email
    subject = 'Thank you for your message to Maya Wilson Photography'
    body = render_to_string(
            'contact/confirmation_emails/confirmation_email_body.txt',
            {'contact': user_contact})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )