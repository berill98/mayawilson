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

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.save()

            return redirect(reverse('contact_success'))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def contact_success(request):

    template = 'contact/contact_success.html'

    return render(request, template)