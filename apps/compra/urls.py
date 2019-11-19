from django.conf.urls import url
from apps.compra.views import index_compra

urlpatterns = [
    url(r'^$',index_compra),
]