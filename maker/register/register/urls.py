"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mainsite import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.index1),
    url(r'^(\d+)/(\w+)/$', views.index1),
    url(r'^index/$', views.index, name='index'),
    url(r'^first/$', views.first, name='first'),
     url(r'^information/$', views.information, name='information'),
    url(r'^second/$', views.second, name='second'),
    url(r'^third/$', views.third, name='third'),
    url(r'^forth/$', views.forth, name='forth'),
    url(r'^fifth/$', views.fifth, name='fifth'),
    url(r'^userinfo/$', views.userinfo),
    url(r'^post/$', views.posting),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
]