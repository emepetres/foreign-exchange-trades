from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.landing, name='trades'),
    url(r'^new_trade/?$', views.new_trade, name='new_trade'),
]
