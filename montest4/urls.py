"""montest4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# import montest4.settings
from login.views import login, logout,index
from devmanage.views import ip_view, add_ip, add_dev, search_dev, search_ip, mod_dev, mod_ip, dev_view
# from devmanage.views import *

admin.autodiscover()
# from django.conf.urls import handler404, handler500

# handler404 = "webserver.views.page_not_found"
# handler500 = "webserver.views.page_error"


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'admin/', include(admin.site.urls)),
    # url(r'', 'views.index',name='index'),
    # url(r'index/', 'views.index',name='index'),
    # url(r'login/', 'views.login',name='login'),
    # url(r'logout/', 'views.logout',name='logout'),
    # url(r'accounts/login', 'views.index',name='index'),
    # url(r'dev_manage/', 'views.dev_view',name='dev_manage'),
    # url(r'ip_manage/', 'views.ip_view'),
    # url(r'add_ip/', 'views.add_ip'),
    # url(r'add_dev/$', 'views.add_dev'),
    # url(r'search_ip/$', 'views.search_ip'),
    # url(r'search_dev/$', 'views.search_dev'),
    # url(r'mod_ip/$', 'views.mod_ip'),
    # url(r'mod_dev/$', 'views.mod_dev',name='mode_dev'),

    # url(r'', include('login.urls')),
    # url(r'index/', include('login.urls')),
    url(r'login/', login),
    url(r'logout/',logout),
    url(r'accounts/login', index),
    url(r'dev_manage/', dev_view),
    url(r'ip_manage/', ip_view),
    url(r'add_ip/', add_ip),
    url(r'add_dev/$', add_dev),
    url(r'search_ip/$',search_ip),
    url(r'search_dev/$',search_dev),
    url(r'mod_ip/$', mod_ip),
    url(r'mod_dev/$', mod_dev),
    url(r'', index),
]