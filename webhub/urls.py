from django.conf.urls import include, url
from rest_framework import routers

from malaria_api import views as malaria_api_views
from pcsa import views as pcsa_views
from pcsa_GHN import views as ghn_views
from pcsa_safety_tools import views as safetytools_views
from profiles import views as profiles_views
from webhub import views
from firstaide import views as firstaide_views
from django.views.generic import RedirectView
from webhub.views import DashboardView, ListUsers, PcuserDetail, AboutPC, Policies, Details, HelpPC, PostSearchView, LoginReal
from profiles.views import ProfileView, EditProfile



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'pcsa_posts', pcsa_views.PcsaPostViewSet)
router.register(r'malaria_posts', malaria_api_views.PostViewSet)
router.register(r'malaria_users', malaria_api_views.MalariaUsersViewSet)
router.register(r'gethelpnow/posts', ghn_views.ghnPostsViewSet)
router.register(r'gethelpnow/contacts', ghn_views.ContactViewSet)
router.register(r'safetytools/posts', safetytools_views.SafetyToolsPostViewSet)
router.register(r'firstaide/(?P<id>.+)', firstaide_views.FirstAideAPIViewSet,'base_name_argument')

urlpatterns = [
    url(r'^$',
        DashboardView.as_view(),
        name='dashboard'),
    url(r'^profile/$',
        ProfileView.as_view(),
        name='profile'),
    url(r'^edit_profile/(?P<pk>\d+)/$',
        EditProfile.as_view(),
        name='edit_profile'),
    url(r'^pcuser/$',
        ListUsers.as_view(),
        name='pcuser_list'),
    url(r'^pcuser/(?P<pk>[0-9]+)/$',
        PcuserDetail.as_view(),
        name='pcuser_detail'),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
    url(r'^api/',
        include(router.urls)),
    url(r'^aboutPC/$',
        AboutPC.as_view(),
        name='aboutPC'),
    url(r'^policies/$',
        Policies.as_view(),
        name='policies'),
    url(r'^details/$',
        Details.as_view(),
        name='details'),
    url(r'^helpPC/$',
        HelpPC.as_view(),
        name='helpPC'),
    url(r'^search/$',
        PostSearchView.as_view(),
        name='search'),
    url(r'^login_real/$', LoginReal.as_view(), name = 'login_real'),
    url(r'^login_social/$', views.login_social, name = 'login_social'),
]
