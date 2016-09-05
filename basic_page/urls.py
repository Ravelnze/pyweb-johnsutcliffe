from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.load_home, name='home'),
    url(r'^reception/', views.load_reception, name='reception')
]
