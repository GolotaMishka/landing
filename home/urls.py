from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'^curse1/$', views.curse1, name='curse1'),
    url(r'^curse2/$', views.curse2, name='curse2'),
    url(r'^curse1/#form_section$', views.curse1, name='curse1'),
    url(r'^curse2/#form_section$', views.curse2, name='curse2'),
]
