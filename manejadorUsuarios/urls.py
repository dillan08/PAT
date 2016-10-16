from django.conf.urls import url
from rest_framework import routers

from manejadorUsuarios.views import PerfilAdministrador
from . import views

router =routers.DefaultRouter(trailing_slash=False)

router.register(r'perfil_admin',PerfilAdministrador,'perfil_admin')

urlpatterns = [
    url(r'^$', views.PerfilList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.PerfilDetail.as_view()),
    #url(r'^/a/(?P<pk>[0-9]+)/$',views.PerfilDetalle.as_view()),
]

urlpatterns +=router.urls
