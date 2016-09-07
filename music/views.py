#Take a User Request and give them back something
#99% User will request a webpage
from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'
    
