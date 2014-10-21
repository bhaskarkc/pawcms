from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.POST:
        pass
    else:
        return render(request, 'contact.html')