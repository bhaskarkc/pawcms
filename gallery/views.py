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


from sitetree.sitetreeapp import register_dynamic_trees, compose_dynamic_tree
from sitetree.utils import tree, item
from gallery import gallery_settings

gallery_tree = (
    tree('gallery', 'Gallery Tree', (
        item('Gallery', 'list_albums', alias='gallery',
             children=(item(album.name, 'view_album ' + album.slug) for album in Album.objects.all()),
             in_menu=gallery_settings.gallery_in_nav),
    )),
)

register_dynamic_trees(
    compose_dynamic_tree(gallery_tree, target_tree_alias='main-nav-menu'),
    reset_cache=True
)

