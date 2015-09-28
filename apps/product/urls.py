from django.conf.urls import patterns, url
from apps.product import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<product_id>\d+)$', views.show, name='show'),
	url(r'^create$', views.create, name='create'),
	url(r'^update/(?P<product_id>\d+)$', views.update, name='update'),
	url(r'^delete/(?P<product_id>\d+)$', views.destroy, name='delete')
)