from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.landing, name='trades'),
    re_path(r'^new_trade/?$', views.new_trade, name='new_trade'),
    re_path(r'^new_trade/get_rate/?$', views.get_rate, name='get_rate'),
]
