from django.conf.urls import url
from rest_framework import routers

from interesesCRUD.views import InteresVS

router =routers.DefaultRouter(trailing_slash=False)

router.register(r'intereses',InteresVS,'intereses')

urlpatterns = []

urlpatterns +=router.urls
