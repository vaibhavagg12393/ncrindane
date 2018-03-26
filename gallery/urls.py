from django.conf.urls import url

from gallery.views import AlbumDetail, gallery
import views


urlpatterns = [
    url(r'^$', gallery, name='gallery'),
    url(r'^(?P<slug>[-\w]+)$', AlbumDetail.as_view(), name='album')
]
