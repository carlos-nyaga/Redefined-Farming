#from django.conf.urls import path, re_path
from django.conf.urls import url

from .views import index
from .apps import ApiConfig

app_name = ApiConfig

urlpatterns = [
url(r'^$', index , name="index"),
]
