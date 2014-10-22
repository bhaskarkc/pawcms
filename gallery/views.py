from django.shortcuts import render, get_object_or_404
from models import Album, Image


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'list_albums.html', {'objects': albums})


def view_album(request, slug):
    album = get_object_or_404(Album, slug=slug)
    return render(request, 'view_album.html', {'album': album})


def view_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    return render(request, 'view_image.html', {'image': image})