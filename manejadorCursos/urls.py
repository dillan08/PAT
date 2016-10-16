from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from manejadorCursos import views
from manejadorCursos.views import CursoViewSet
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gestionCursos', CursoViewSet, 'gestionCursos')
urlpatterns = [
    url(r'^$', views.CursosList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.CursoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += router.urls