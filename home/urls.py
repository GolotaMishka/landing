from django.conf.urls import url, include
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^$', views.curse1, name='curse1'),
    url(r'^#form_section$', views.curse1, name='curse1'),
]
