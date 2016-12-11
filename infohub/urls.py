from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('webhub.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^malaria/', include('malaria_web.urls', namespace='malaria')),
    url(r'^webhub/', include('webhub.urls', namespace='webhub')),
    url(r'^signup/', include('signup.urls', namespace='signup')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    url(r'^pcsa/', include('pcsa.urls', namespace='pcsa')),
    url(r'^gethelpnow/', include('pcsa_GHN.urls', namespace='pcsa_GHN')),
    url(r'^safetytools/', include('pcsa_safety_tools.urls', namespace='pcsa_safety_tools'))
)
