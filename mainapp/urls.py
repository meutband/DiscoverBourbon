from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^facts', views.facts, name='facts'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^admin', include(admin.site.urls)),
    url(r'^bourbons/', include('bourbonsite.urls', namespace='bourbonsite')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls', namespace="auth")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
