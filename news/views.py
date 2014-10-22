from django.shortcuts import render
from models import News


def list_news(request):
    objects = News.objects.filter(status='Published')
    return render(request, 'list_news.html', {'objects': objects})

