"""loco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import ListView
from osm.models import Banks
from djgeojson.views import GeoJSONLayerView
from django.contrib.gis.measure import D

bancos_barranquilla = Banks.objects.filter(wkb_geometry__distance_lte=(barranquilla, D(km=20)))

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=bancos_barranquilla, template_name='osm/banks.html')),
    url(r'^banks$', GeoJSONLayerView.as_view(model=Banks), name='data'),
    url(r'^admin/', include(admin.site.urls)),
]
