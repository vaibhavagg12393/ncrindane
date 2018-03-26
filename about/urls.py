from django.conf.urls import url

import views


urlpatterns = [
    url('/here/', views.index, name='index')
]
