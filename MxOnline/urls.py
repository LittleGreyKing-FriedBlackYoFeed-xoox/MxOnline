from django.conf.urls import url
from django.contrib import admin
import xadmin
# from extra_apps import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
]
