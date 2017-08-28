from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit_quote$', views.submit_quote),
    url(r'^logout$', views.logout),
    url(r'^add_quote/(?P<quote_id>\d+)/(?P<user_id>\d+)$', views.add_quote),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^remove_quote/(?P<quote_id>\d+)/(?P<user_id>\d+)$', views.remove_quote),
]