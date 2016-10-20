from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from manejadorOATs import views
from manejadorOATs.views import OATsViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gestionOAT', OATsViewSet, 'gestionOAT')

urlpatterns = [
    # url(r'^$', views.OATList.as_view()),
    # url(r'^(?P<pk>[0-9]+)/$', views.OATDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls