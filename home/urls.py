from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^individual/$', views.curse1, name='curse1'),
    url(r'^group/$', views.curse2, name='curse2'),
    url(r'^individual/#form_section$', views.curse1, name='curse1'),
    url(r'^group/#form_section$', views.curse2, name='curse2'),
]
