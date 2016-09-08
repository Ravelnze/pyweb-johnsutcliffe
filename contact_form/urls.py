from django.conf.urls import url
import views

urlpatterns = [
    url(r'^', views.load_form, name='form'),
    url(r'^thanks/', views.complete_form, name='complete'),
]
