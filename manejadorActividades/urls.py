from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from manejadorActividades import views

urlpatterns = [
    url(r'^$', views.ActividadList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ActividadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)