from . import views
from django.conf.urls import url
# from main.views import (MainView, PostView, RsvpView)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^about/', views.about, name='about'),
    # url(r'^photos/', PhotoView.as_view(), name='photos'),
]
