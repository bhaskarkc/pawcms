from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from socket import error as socket_error


def home(request):
    return render(request, 'home.html')


def contact(request):
    message = None
    if request.POST:
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email', '')

        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['contact@devchuli.edu.np'])
                message = 'Thank You for the message!'
            except BadHeaderError:
                message = 'Invalid Data Submitted!'
            except socket_error as the_error:
                if the_error.errno != 111:
                    raise the_error
                message = 'Couldn\'t send Email'
        else:
            message = 'Please fill in the required fields!'
            return render(request, 'contact.html', {'message': message})
    return render(request, 'contact.html', {'message': message})