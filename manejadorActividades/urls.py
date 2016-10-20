#from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
#from manejadorActividades import views
from rest_framework import routers
from manejadorActividades.views import ActividadVS

router =routers.DefaultRouter(trailing_slash=False)
router.register(r'actividades',ActividadVS,'actividades')


urlpatterns = [
    #url(r'^$', views.ActividadList.as_view()),
    #url(r'^(?P<pk>[0-9]+)/$', views.ActividadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns +=router.urls