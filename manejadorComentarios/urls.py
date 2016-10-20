
from rest_framework import routers

from manejadorComentarios.views import ComentariosVS
from . import views

router =routers.DefaultRouter(trailing_slash=False)

router.register(r'comentarios',ComentariosVS,'comentarios')

urlpatterns = [
]

urlpatterns +=router.urls
