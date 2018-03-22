from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^vendors/$', views.vendors, name='vendors'),
	url(r'^services/$', views.services, name='services'),
	url(r'^media/$', views.media, name='media'),
	]