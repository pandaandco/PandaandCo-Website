from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^website/', include('website.urls')),
    url(r'^$', views.index, name='index'),
]
