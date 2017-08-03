from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$',views.login),
    url(r'^register/$', views.register),
    url(r'register_handle/$',views.register_handle),
    url(r'check_name/$',views.check_name),
    url(r'login_handle/$',views.login_handle),
    url(r'center/$',views.center),
    url(r'site/$',views.site),
    url(r'order/$',views.order),
    url(r'logout/$', views.logout),

]
