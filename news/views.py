from django.shortcuts import render, get_object_or_404
from models import News


def list_news(request):
    objects = News.objects.filter(status='Published').order_by('-date')
    return render(request, 'list_news.html', {'objects': objects})


def view_news(request, slug):
    obj = get_object_or_404(News, slug=slug, status='Published')
    return render(request, 'view_news.html', {'obj': obj})