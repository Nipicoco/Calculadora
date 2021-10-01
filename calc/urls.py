from django.conf.urls import url
from calc import views
from django.urls import path
from .views import index, reproductor


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path("video", views.reproductor, name='video')
    
]
