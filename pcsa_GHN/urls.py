from django.conf.urls import url

from pcsa_GHN import views
from pcsa_GHN.views import CreatePostView, UpdatePostView, DeletePostView, ViewPostView, ListPostView
from pcsa_GHN.views import CreateContactView, UpdateContactView, DeleteContactView, ViewContactView

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

    url(r'^create_contact/$',
        CreateContactView.as_view(),
        name = 'create_contact'),

    url(r'^delete_contact/(?P<pk>\d+)$',
        DeleteContactView.as_view(),
        name='delete_contact'),

    url(r'^edit_contact/(?P<pk>\d+)$',
        UpdateContactView.as_view(),
        name='edit_contact'),

    url(r'^view_contact/(?P<pk>\d+)$',
        ViewContactView.as_view(),
        name='view_contact'),

    url(r'^$',
        ListPostView.as_view(),
        name = 'home')
]
