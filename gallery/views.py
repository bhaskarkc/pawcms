from django.shortcuts import render
from models import Album, Image


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'list_albums.html', {'objects': albums})


def view_album(request):
    pass


def view_image(request):
    pass