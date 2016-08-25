from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.load_page, name='basic_page'),
]
