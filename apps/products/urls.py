from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^new', views.new, name="new"),
	url(r'^create', views.create, name="create"),
	url(r'^product/(?P<product_id>\d+)/$', views.product, name="product"),
	url(r'^edit/(?P<product_id>\d+)/$', views.edit, name="edit"),
	url(r'^remove/(?P<product_id>\d+)/$', views.remove, name="remove"),
	url(r'^update/(?P<product_id>\d+)/$', views.update, name="update"),
]