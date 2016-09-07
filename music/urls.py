from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/71/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),


    # /music/<album_id>/favorite/
#    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
