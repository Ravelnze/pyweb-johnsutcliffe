from django.conf.urls import url
import views


urlpatterns = [
    url(r'^reception/$', views.reception, name='reception'),
    url(r'^music/$', views.music, name='music'),
    url(r'^$', views.home, name='home'),
]

