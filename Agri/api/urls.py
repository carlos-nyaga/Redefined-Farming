#from django.conf.urls import path, re_path
from django.conf.urls import url

from .views import IndexView
from .apps import ApiConfig

app_name = ApiConfig

urlpatterns = [
url(r'^index', IndexView.as_view(), name="index")]
