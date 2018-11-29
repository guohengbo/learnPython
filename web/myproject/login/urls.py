from django.contrib import admin
from django.conf.urls import url
from . import views

app_name='login'
urlpatterns = [
# ex : /login/
url(r'^$', views.login, name='login'),
]