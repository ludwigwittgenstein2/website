from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]
