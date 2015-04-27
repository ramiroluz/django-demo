from django.conf.urls import include, url
from django.contrib import admin
from sinucao.settings import MEDIA_ROOT

urlpatterns = [
    # Examples:
    # url(r'^$', 'sinucao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^reservas/', include('reserva.urls', namespace='reservas')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT})
]


