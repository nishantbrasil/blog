from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', auth_views.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}, name='logout'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<slug>\w+)/$', views.post_user, name='post_user'),
    url(r'^q=(?P<slug>)/$', views.post_detail, name='post_user'),
]