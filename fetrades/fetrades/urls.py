from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    re_path(r'^', include('trades.urls'))
]
