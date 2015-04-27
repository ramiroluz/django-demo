from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/$', views.ListaView.as_view(), name='lista'),
    url(r'^cliente/(?P<pk>[0-9]+)/$',
        views.ClienteView.as_view(),
        name='cliente'),
    url(r'^reserva/(?P<pk>[0-9]+)/$',
        views.ReservaView.as_view(),
        name='reserva'),
]
