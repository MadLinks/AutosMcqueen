from django.conf.urls import url, include
from apps.auto.views import index, auto_view, auto_listar, auto_editar, auto_eliminar, quienesSomos, contacto
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^index$', login_required(index), name='index' ),
    url(r'^quienesSomos$', login_required(quienesSomos), name='quienesSomos' ),
    url(r'^contacto$', login_required(contacto), name='contacto' ),
    url(r'^nuevo$', login_required(auto_view), name='auto_crear'),
    url(r'^listar$', (auto_listar), name='auto_listar'),
    url(r'^editar/(?P<id_auto>\d+)/$', login_required(auto_editar), name='auto_editar'),
    url(r'^eliminar/(?P<id_auto>\d+)/$', login_required(auto_eliminar), name='auto_eliminar')
]