from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^test/(?P<user_id>\d+)$', views.test),
    url(r'^reset$', views.reset)
]
