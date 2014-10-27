from django.shortcuts import render
from models import File


def list_files(request):
    objects = File.objects.filter(status='Published').order_by('-date')
    return render(request, 'list_files.html', {'objects': objects})