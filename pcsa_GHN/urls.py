from django.conf.urls import patterns, url
from pcsa_GHN import views

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

    url(r'^create_contact/$',
        views.create_contact,
        name = 'create_contact'),
    url(r'^delete_contact/(?P<contact_id>\d+)$',
        views.delete_contact,
        name='delete_contact'),

    url(r'^edit_contact/(?P<contact_id>\d+)$',
        views.edit_contact,
        name='edit_contact'),
    url(r'^view_contact/(?P<contact_id>\d+)$',
        views.view_contact,
        name='view_contact'),
    url(r'^$',
        views.home,
        name = 'home')
)
