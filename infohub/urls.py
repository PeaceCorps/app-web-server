from django.conf.urls import include, url
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

admin.autodiscover()
schema_view = get_swagger_view(title='Swagger API') 

# Inlude URLs from other apps here
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('webhub.urls')),
    url(r'^docs/', schema_view),
    url(r'^malaria/', include('malaria_web.urls', namespace='malaria')),
    url(r'^webhub/', include('webhub.urls', namespace='webhub')),
    url(r'^pcsa/', include('pcsa.urls', namespace='pcsa')),
    url(r'^gethelpnow/', include('pcsa_GHN.urls', namespace='pcsa_GHN')),
    url(r'^firstaide/', include('firstaide.urls', namespace='firstaide')),
    url(r'^safetytools/', include('pcsa_safety_tools.urls', namespace='pcsa_safety_tools')),
    url(r'^accounts/', include('allauth.urls')),
    url('', include('social_django.urls', namespace='social'))
]
