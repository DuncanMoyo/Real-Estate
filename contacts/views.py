from django.shortcuts import render, redirect
from .forms import ContactsForm
from django.core.mail import send_mail, BadHeaderError
from EstateAgency.settings import base
from django.template.loader import get_template
from django.contrib import messages


def contact_us(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST or None)
        if form.is_valid():

            name = request.POST.get('name')
            email = request.POST.get('email')
            what_subject = request.POST.get('subject')
            message = request.POST.get('message')

            # email ourselves the submitted contact message

            subject = 'Contact Form Received'
            from_email = email
            to_email = [base.DEFAULT_FROM_EMAIL]

            # # OPTION 1
            # contact_message = "{0}, from {1} with email {2}".format(message, name, email, what_subject)

            # OPTION 2

            context = {
                'name': name,
                'email': email,
                'what_subject': what_subject,
                'message': message,
            }

            contact_message = get_template('contact_message.txt').render(context)

            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

            # messages.success('Your message has been sent!')
            return redirect("/contact/")
    form = ContactsForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)


