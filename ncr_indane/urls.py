from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import app.forms
import app.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^enquiry/', include('enquiry.urls', namespace='enquiry')),
    url(r'^complaint/', include('complaint.urls', namespace='complaint')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^faq/', include('faq.urls', namespace='faq')),
    url(r'^app/', include('app.urls', namespace='gallery')),
    # url(r'^contact/', include('contact.urls', namespace='contact')),
    # url(r'^organize/', include('organize.urls', namespace='organize')),
    # url(r'^story/', include('story.urls', namespace='story')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
