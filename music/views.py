#Take a User Request and give them back something
#99% User will request a webpage
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
    all_albums = Album.objects.all()
#Information that your template needs
    return render(request, 'music/index.html', {'all_albums': all_albums,
    })


def detail(request, album_id):
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
