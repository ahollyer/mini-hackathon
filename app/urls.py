from django.conf.urls import include, url
from django.contrib import admin
from homepage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^2017/', include('homepage.urls', namespace='homepage')),
]
