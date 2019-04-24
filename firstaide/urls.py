from django.conf.urls import url
from .views import *

# Connect URLs to Views here
urlpatterns = [
	    url(r'^$',
        ListFirstAideAPIView.as_view(),
        name = 'first_aide_api_home'),

	    url(r'^create/$',
        CreateFirstAideAPIView.as_view(),
        name='first_aide_api_create'),

        url(r'^delete_post/(?P<pk>\d+)$',
        DeleteFirstAideAPIView.as_view(),
        name='first_aide_api_delete_post'),
 
        url(r'^edit_post/(?P<pk>\d+)$',
        UpdateFirstAideAPIView.as_view(),
        name='first_aide_api_edit_post'),

	    url(r'^view_post/(?P<pk>\d+)$',
        ViewFirstAideAPIView.as_view(),
        name='first_aide_api_view_post'),

]

"""
    (?P<pk>\d+ explained -
    In Python regular expressions, the syntax for named regular-expression groups is 
    (?P<name>pattern), where name is the name of the group and pattern is some pattern to match.
    Here pattern is d+ (decimal digits 1 or more eg 0, 11 , 463). Hence, ?P<pk>5 will render value of pk as 5
    
"""