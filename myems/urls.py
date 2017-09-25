from django.conf.urls import url
from . import views

app_name = 'myems'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^roster/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^roster/table/$', views.table, name='table'),
]
