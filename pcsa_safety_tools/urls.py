from django.conf.urls import patterns, url
from pcsa_safety_tools import views

urlpatterns = patterns(
    '',
    url(r'^create_post/$',
        views.create_post,
        name='create_post'),

    url(r'^delete_post/(?P<post_id>\d+)$',
        views.delete_post,
        name='delete_post'),

    url(r'^edit_post/(?P<post_id>\d+)$',
        views.edit_post,
        name='edit_post'),

    url(r'^view_post/(?P<post_id>\d+)$',
        views.view_post,
        name='view_post'),
    url(r'^home/$', views.home, name='home')
)