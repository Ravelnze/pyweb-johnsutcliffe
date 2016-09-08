from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^enquiries/', include('contact_form.urls', namespace='contact')),
    url(r'^', include('basic_page.urls', namespace='basic_page')),
]
