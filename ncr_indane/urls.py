from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^enquiry/', include('enquiry.urls', namespace='enquiry')),
    url(r'^complaint/', include('complaint.urls', namespace='complaint')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
    url(r'^faq/', include('faq.urls', namespace='faq')),
    # url(r'^contact/', include('contact.urls', namespace='contact')),
    # url(r'^organize/', include('organize.urls', namespace='organize')),
    # url(r'^story/', include('story.urls', namespace='story')),
]
