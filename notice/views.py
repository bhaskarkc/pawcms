from django.shortcuts import render, get_object_or_404
from models import Notice


def list_notices(request):
    objects = Notice.objects.filter(status='Published').order_by('-date')
    return render(request, 'list_notices.html', {'objects': objects})


def view_notice(request, slug):
    obj = get_object_or_404(Notice, slug=slug, status='Published')
    return render(request, 'view_notice.html', {'obj': obj})