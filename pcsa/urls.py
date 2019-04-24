from django.conf.urls import include, url
from rest_framework import routers

from pcsa import views
from pcsa_GHN import views as ghn_views
from pcsa.views import ListPostView, CreatePostView, UpdatePostView, DeletePostView, ViewPostView

urlpatterns = [
    url(r'^create_post/$',
        CreatePostView.as_view(),
        name='create_post'),

    url(r'^delete_post/(?P<pk>\d+)$',
        DeletePostView.as_view(),
        name='delete_post'),

    url(r'^edit_post/(?P<pk>\d+)$',
        UpdatePostView.as_view(),
        name='edit_post'),

    url(r'^list_posts/$',
        ListPostView.as_view(),
        name='list_posts'),

    url(r'^view_post/(?P<pk>\d+)$',
        ViewPostView.as_view(),
        name='view_post'),

]
