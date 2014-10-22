from django.shortcuts import render
from models import Application
from forms import ApplicationForm


def apply_online(request):
    message = None
    if request.POST:
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            message = 'Your application has been received. Thank You!'
    else:
        form = ApplicationForm()
    return render(request, 'application_form.html', {'form': form, 'message': message})




