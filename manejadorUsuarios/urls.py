from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.PerfilList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',views.PerfilDetail.as_view()),
]
