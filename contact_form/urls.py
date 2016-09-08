from django.conf.urls import url
import views

urlpatterns = [
    url(r'^thanks/', views.complete_form, name='complete'),
    url(r'^', views.load_form, name='form'),
]
