from django.conf.urls import url

from pcsa_safety_tools import views
from pcsa_safety_tools.views import CreatePostView, UpdatePostView, DeletePostView, ViewPostView, ListPostView

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

    url(r'^view_post/(?P<pk>\d+)$',
        ViewPostView.as_view(),
        name='view_post'),

    url(r'^home/$', 
        ListPostView.as_view(), 
        name='home')
]
